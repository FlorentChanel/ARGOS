import re
from dataclasses import asdict, dataclass
from typing import cast


def _require_str(data: dict[str, object], key: str, ctx: str) -> str:
    value = data.get(key)
    if not isinstance(value, str):
        raise ValueError(f"{ctx}.{key} must be a string, got {type(value).__name__!r}")
    return value


def _require_int(data: dict[str, object], key: str, ctx: str) -> int:
    value = data.get(key)
    if not isinstance(value, int):
        raise ValueError(f"{ctx}.{key} must be an int, got {type(value).__name__!r}")
    return value


def _require_list(data: dict[str, object], key: str, ctx: str) -> list[object]:
    value = data.get(key, [])
    if not isinstance(value, list):
        raise ValueError(f"{ctx}.{key} must be a list, got {type(value).__name__!r}")
    return cast(list[object], value)


def _optional_int(data: dict[str, object], key: str, ctx: str) -> int | None:
    value = data.get(key)
    if value is None:
        return None
    if not isinstance(value, int):
        raise ValueError(
            f"{ctx}.{key} must be an int or null, got {type(value).__name__!r}"
        )
    return value


def _optional_str(data: dict[str, object], key: str, ctx: str) -> str | None:
    value = data.get(key)
    if value is None:
        return None
    if not isinstance(value, str):
        raise ValueError(
            f"{ctx}.{key} must be a string or null, got {type(value).__name__!r}"
        )
    return value


@dataclass(frozen=True)
class ExerciseResult:
    exercise_id: str
    exercise_name: str
    skills: list[str]
    points_earned: int
    points_available: int
    total_tests: int | None
    failed_tests: int | None
    compilation_output: str | None
    test_results: list[dict[str, object]] | None
    gtest_output: str | None
    tampered: bool = False

    @classmethod
    def from_json(cls, data: object) -> "ExerciseResult":
        if not isinstance(data, dict):
            raise TypeError(
                f"ExerciseResult: expected dict, got {type(data).__name__!r}"
            )
        d = cast(dict[str, object], data)
        skills_raw = _require_list(d, "skills", "ExerciseResult")
        if not all(isinstance(s, str) for s in skills_raw):
            raise ValueError("ExerciseResult.skills must be a list of strings")
        return cls(
            exercise_id=_require_str(d, "exercise_id", "ExerciseResult"),
            exercise_name=_require_str(d, "exercise_name", "ExerciseResult"),
            skills=cast(list[str], skills_raw),
            points_earned=_require_int(d, "points_earned", "ExerciseResult"),
            points_available=_require_int(d, "points_available", "ExerciseResult"),
            total_tests=_optional_int(d, "total_tests", "ExerciseResult"),
            failed_tests=_optional_int(d, "failed_tests", "ExerciseResult"),
            compilation_output=_optional_str(d, "compilation_output", "ExerciseResult"),
            test_results=cast(list[dict[str, object]] | None, d.get("test_results")),
            gtest_output=_optional_str(d, "gtest_output", "ExerciseResult"),
            tampered=bool(d.get("tampered", False)),
        )


@dataclass(frozen=True)
class SerieResult:
    name: str
    points_earned: int
    points_to_complete: int
    exercises: list[ExerciseResult]

    @property
    def completed(self) -> bool:
        return self.points_earned >= self.points_to_complete

    @classmethod
    def from_json(cls, data: object) -> "SerieResult":
        if not isinstance(data, dict):
            raise TypeError(f"SerieResult: expected dict, got {type(data).__name__!r}")
        d = cast(dict[str, object], data)
        exercises_raw = _require_list(d, "exercises", "SerieResult")
        return cls(
            name=_require_str(d, "name", "SerieResult"),
            points_earned=_require_int(d, "points_earned", "SerieResult"),
            points_to_complete=_require_int(d, "points_to_complete", "SerieResult"),
            exercises=[ExerciseResult.from_json(e) for e in exercises_raw],
        )


@dataclass(frozen=True)
class LearningPathResult:
    id: str
    name: str
    series: list[SerieResult]

    @classmethod
    def from_json(cls, data: object) -> "LearningPathResult":
        if not isinstance(data, dict):
            raise TypeError(
                f"LearningPathResult: expected dict, got {type(data).__name__!r}"
            )
        d = cast(dict[str, object], data)
        series_raw = _require_list(d, "series", "LearningPathResult")
        return cls(
            id=_require_str(d, "id", "LearningPathResult"),
            name=_require_str(d, "name", "LearningPathResult"),
            series=[SerieResult.from_json(s) for s in series_raw],
        )


@dataclass(frozen=True)
class ScoreSummary:
    learning_paths: list[LearningPathResult]

    @classmethod
    def from_json(cls, data: object) -> "ScoreSummary":
        if not isinstance(data, dict):
            raise TypeError(f"ScoreSummary: expected dict, got {type(data).__name__!r}")
        d = cast(dict[str, object], data)
        lps_raw = _require_list(d, "learning_paths", "ScoreSummary")
        return cls(learning_paths=[LearningPathResult.from_json(lp) for lp in lps_raw])

    def to_json(self) -> dict[str, object]:
        return {
            "learning_paths": [
                {
                    "id": lp.id,
                    "name": lp.name,
                    "series": [
                        {
                            "name": serie.name,
                            "points_earned": serie.points_earned,
                            "points_to_complete": serie.points_to_complete,
                            "completed": serie.completed,
                            "exercises": [asdict(ex) for ex in serie.exercises],
                        }
                        for serie in lp.series
                    ],
                }
                for lp in self.learning_paths
            ]
        }

    def to_str(self) -> str:
        sep = "─" * 44
        lines: list[str] = ["📊 Score Summary", sep]

        for lp in self.learning_paths:
            checked_series = [serie for serie in lp.series if serie.exercises]
            if not checked_series:
                continue
            lines.append(lp.name)
            for serie in checked_series:
                icon = "✅" if serie.completed else "❌"
                status = "completed" if serie.completed else "not completed"
                lines.append(
                    f"  {icon} {serie.name}  {serie.points_earned}/{serie.points_to_complete} pts  {status}"
                )
                for ex in serie.exercises:
                    ex_icon = "✅" if ex.points_earned > 0 else "❌"
                    pts = f"{ex.points_earned}/{ex.points_available} pts"
                    if ex.total_tests is None:
                        tests = "N/A"
                    else:
                        passed = ex.total_tests - (ex.failed_tests or 0)
                        tests = f"{passed}/{ex.total_tests} tests"
                    lines.append(
                        f"    {ex_icon} {ex.exercise_id:<30} {pts:<12} ({tests})"
                    )
            lines.append(sep)

        return "\n".join(lines)

    def failures_to_str(self, exercise_ids: set[str]) -> str:
        """Compiler output or failed tests of the given exercises; '' when none of them failed."""
        blocks: list[str] = []
        seen: set[str] = set()
        for lp in self.learning_paths:
            for serie in lp.series:
                for ex in serie.exercises:
                    if ex.exercise_id in seen or ex.exercise_id not in exercise_ids:
                        continue
                    seen.add(ex.exercise_id)
                    block = _failure_block(ex)
                    if block:
                        blocks.append(block)
        return "\n\n".join(blocks)


def _indent(text: str, prefix: str) -> str:
    return "\n".join(prefix + line for line in text.rstrip().splitlines())


_ANSI = re.compile(r"\x1b\[[0-9;]*[A-Za-z]")
_NINJA_LINE = re.compile(r"^(ninja: |\[\d+/\d+\] |FAILED: )")


def _compiler_diagnostics(ninja_output: str) -> str:
    """The compiler messages only: ninja's progress lines and the failed command lines are noise for students."""
    kept: list[str] = []
    after_failed = False
    for line in ninja_output.splitlines():
        plain = _ANSI.sub("", line)
        if after_failed:
            after_failed = False
            continue
        if _NINJA_LINE.match(plain):
            after_failed = plain.startswith("FAILED: ")
            continue
        kept.append(line)
    return "\n".join(kept).strip("\n") or ninja_output


def _failure_block(ex: ExerciseResult) -> str:
    title = f"❌ {ex.exercise_id} {ex.exercise_name}"
    if ex.test_results is None:
        if not ex.compilation_output:
            return ""
        diagnostics = _compiler_diagnostics(ex.compilation_output)
        return f"{title}: compilation failed\n{_indent(diagnostics, '    ')}"
    failed = [t for t in ex.test_results if not t.get("success")]
    if not failed:
        return ""
    lines = [f"{title}: {len(failed)}/{ex.total_tests} tests failed"]
    for test in failed:
        lines.append(f"  🔴 {test['name']}")
        message = test.get("message")
        if isinstance(message, str) and message.strip():
            lines.append(_indent(message, "      "))
    return "\n".join(lines)
