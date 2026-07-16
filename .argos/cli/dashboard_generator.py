import json
from dataclasses import asdict
from pathlib import Path
from typing import Any, cast

from git_bindings import GitBindings
from scoring.score_summary import (
    ExerciseResult,
    LearningPathResult,
    ScoreSummary,
    SerieResult,
)

_COLORS = ["#4f8ef7", "#38d9a9", "#f7c948", "#f06a6a"]


class DashboardGenerator:
    def __init__(self, git_bindings: GitBindings) -> None:
        self._git_bindings = git_bindings

    def generate(self, summary: ScoreSummary, output_path: Path) -> None:
        existing = self._read_existing_summary(output_path)
        merged = self._merge_summaries(existing, summary) if existing else summary
        data = self._build_data(merged)
        js = f"window.ARGOS_DATA = {json.dumps(data, indent=4, ensure_ascii=False)};\n"
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(js, encoding="utf-8")

    def _read_existing_summary(self, output_path: Path) -> ScoreSummary | None:
        if not output_path.exists():
            return None
        content = output_path.read_text(encoding="utf-8")
        prefix = "window.ARGOS_DATA = "
        if not content.startswith(prefix):
            return None
        try:
            raw = json.loads(content[len(prefix) :].rstrip().rstrip(";"))
            lps_raw = raw.get("learningPaths")
            if not isinstance(lps_raw, list):
                return None
            return ScoreSummary.from_json(
                {"learning_paths": cast(list[object], lps_raw)}
            )
        except (json.JSONDecodeError, ValueError, TypeError):
            return None

    def _merge_summaries(
        self, existing: ScoreSummary, new: ScoreSummary
    ) -> ScoreSummary:
        lps_by_id = {lp.id: lp for lp in existing.learning_paths}
        for new_lp in new.learning_paths:
            if new_lp.id not in lps_by_id:
                lps_by_id[new_lp.id] = new_lp
            else:
                lps_by_id[new_lp.id] = self._merge_lp(lps_by_id[new_lp.id], new_lp)
        return ScoreSummary(learning_paths=list(lps_by_id.values()))

    def _merge_lp(
        self, existing: LearningPathResult, new: LearningPathResult
    ) -> LearningPathResult:
        series_by_name = {s.name: s for s in existing.series}
        for new_serie in new.series:
            if new_serie.name not in series_by_name:
                series_by_name[new_serie.name] = new_serie
            else:
                series_by_name[new_serie.name] = self._merge_serie(
                    series_by_name[new_serie.name], new_serie
                )
        return LearningPathResult(
            id=existing.id, name=existing.name, series=list(series_by_name.values())
        )

    def _merge_serie(self, existing: SerieResult, new: SerieResult) -> SerieResult:
        exercises_by_id: dict[str, ExerciseResult] = {
            e.exercise_id: e for e in existing.exercises
        }
        for ex in new.exercises:
            exercises_by_id[ex.exercise_id] = ex
        updated = list(exercises_by_id.values())
        return SerieResult(
            name=existing.name,
            points_earned=sum(e.points_earned for e in updated),
            points_to_complete=existing.points_to_complete,
            exercises=updated,
        )

    def _build_data(self, summary: ScoreSummary) -> dict[str, Any]:
        username = self._git_bindings.get_github_username()
        if username is None or "He-Arc":
            username = self._git_bindings.get_user_name()

        return {
            "username": username,
            "learningPaths": [
                self._build_learning_path(lp, i)
                for i, lp in enumerate(summary.learning_paths)
            ],
        }

    def _build_learning_path(
        self, lp: LearningPathResult, index: int
    ) -> dict[str, Any]:
        series = [self._build_serie(s) for s in lp.series]
        return {
            "id": lp.id,
            "name": lp.name,
            "color": _COLORS[index % len(_COLORS)],
            "active": index == 0,
            "progression": {
                "completed": sum(s.points_earned for s in lp.series),
                "total": sum(
                    e.points_available for s in lp.series for e in s.exercises
                ),
            },
            "series": series,
            "skills": self._build_skills(lp),
        }

    def _build_serie(self, comp: SerieResult) -> dict[str, Any]:
        exercises = [
            {**{k: v for k, v in asdict(ex).items() if k != "test_results"}, "passed": ex.points_earned > 0}
            for ex in comp.exercises
        ]
        return {
            **asdict(comp),
            "points_available": sum(e.points_available for e in comp.exercises),
            "completed": comp.completed,
            "exercises": exercises,
        }

    def _build_skills(self, lp: LearningPathResult) -> list[dict[str, Any]]:
        earned: dict[str, int] = {}
        available: dict[str, int] = {}
        for serie in lp.series:
            for ex in serie.exercises:
                for skill in ex.skills:
                    earned[skill] = earned.get(skill, 0) + ex.points_earned
                    available[skill] = available.get(skill, 0) + ex.points_available
        return [
            {
                "name": name,
                "points_earned": earned[name],
                "points_available": available[name],
            }
            for name in available
        ]
