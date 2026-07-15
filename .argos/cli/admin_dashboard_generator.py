import json
from dataclasses import asdict
from pathlib import Path
from typing import Any

from config.models import LearningPath, Student
from scoring.score_summary import ScoreSummary, SerieResult


class AdminDashboardGenerator:
    def generate(
        self,
        lp: LearningPath,
        scores: dict[str, ScoreSummary],
        invalid_students: list[Student],
        output_path: Path,
    ) -> None:
        data = self._build_data(lp, scores, invalid_students)
        js = f"window.ARGOS_ADMIN_DATA = {json.dumps(data, indent=4, ensure_ascii=False)};\n"
        output_path.write_text(js, encoding="utf-8")

    def _build_data(
        self,
        lp: LearningPath,
        scores: dict[str, ScoreSummary],
        invalid_students: list[Student],
    ) -> dict[str, Any]:
        students = [
            self._build_student(student_name, summary, lp)
            for student_name, summary in scores.items()
        ] + [
            {"username": s.name, "valid_repo": False, "total_earned": None, "total_available": None, "series": []}
            for s in invalid_students
        ]
        return {
            "learningPath": {"id": lp.id, "name": lp.name},
            "series": [s.name for s in lp.series],
            "students": students,
        }

    def _build_student(
        self,
        username: str,
        summary: ScoreSummary,
        lp: LearningPath,
    ) -> dict[str, Any]:
        lp_result = next((r for r in summary.learning_paths if r.id == lp.id), None)
        if lp_result is None:
            return {"username": username, "valid_repo": False, "total_earned": None, "total_available": None, "series": []}

        series = [self._build_serie(s) for s in lp_result.series]
        total_earned = sum(s.points_earned for s in lp_result.series)
        total_available = sum(e.points_available for s in lp_result.series for e in s.exercises)
        any_tampered = any(ex.tampered for s in lp_result.series for ex in s.exercises)
        return {
            "username": username,
            "valid_repo": True,
            "total_earned": total_earned,
            "total_available": total_available,
            "any_tampered": any_tampered,
            "series": series,
        }

    def _build_serie(self, serie: SerieResult) -> dict[str, Any]:
        exercises = [
            {**{k: v for k, v in asdict(ex).items() if k != "test_results"}, "passed": ex.points_earned > 0}
            for ex in serie.exercises
        ]
        return {
            "name": serie.name,
            "points_earned": serie.points_earned,
            "points_to_complete": serie.points_to_complete,
            "points_available": sum(e.points_available for e in serie.exercises),
            "completed": serie.completed,
            "exercises": exercises,
        }
