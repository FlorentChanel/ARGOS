from dataclasses import asdict, dataclass
from enum import StrEnum
from typing import Any, Generic, TypeVar

from tests.models import TestSuite


class StepName(StrEnum):
    """Stable identifiers for pipeline steps (display labels and JSON keys)."""

    CMAKE = "cmake"
    NINJA = "ninja"
    UNIT_TESTS = "unit_tests"


@dataclass(frozen=True)
class EmptyPayload:
    """Payload for steps that carry no extra data (e.g. cmake)."""


@dataclass(frozen=True)
class NinjaPayload:
    compilation_output: str | None = None


@dataclass(frozen=True)
class UnitTestsPayload:
    # ``suite`` is ``None`` when the test runner failed to execute. Everything
    # else (test counts, gtest output) is derived from the suite by consumers.
    suite: TestSuite | None = None


PayloadT = TypeVar("PayloadT")


@dataclass(frozen=True)
class StepResult(Generic[PayloadT]):
    success: bool
    skipped: bool
    formatted_data: str
    data: PayloadT


@dataclass(frozen=True)
class ExerciseStepResults:
    ninja: StepResult[NinjaPayload]
    unit_tests: StepResult[UnitTestsPayload]


def _icon(result: StepResult[Any]) -> str:
    return "⏭" if result.skipped else ("✅" if result.success else "❌")


def _result_json(result: StepResult[Any]) -> dict[str, object]:
    return {
        "success": result.success,
        "skipped": result.skipped,
        "data": asdict(result.data),
    }


@dataclass(frozen=True)
class PipelineReport:
    cmake: StepResult[EmptyPayload]
    exercise_results: dict[str, ExerciseStepResults]

    @property
    def overall_success(self) -> bool:
        if not (self.cmake.success or self.cmake.skipped):
            return False
        return all(
            result.success or result.skipped
            for steps in self.exercise_results.values()
            for result in (steps.ninja, steps.unit_tests)
        )

    def to_json(self) -> dict[str, object]:
        return {
            "global": {StepName.CMAKE: _result_json(self.cmake)},
            "exercises": {
                ex_id: {
                    StepName.NINJA: _result_json(steps.ninja),
                    StepName.UNIT_TESTS: _result_json(steps.unit_tests),
                }
                for ex_id, steps in self.exercise_results.items()
            },
        }

    def to_str(self) -> str:
        lines: list[str] = []

        lines.append(f"{_icon(self.cmake)} {StepName.CMAKE}")
        if self.cmake.formatted_data:
            lines.append(f"   {self.cmake.formatted_data}")

        for ex_id, steps in self.exercise_results.items():
            lines.append(f"\n{ex_id}")
            for name, result in (
                (StepName.NINJA, steps.ninja),
                (StepName.UNIT_TESTS, steps.unit_tests),
            ):
                lines.append(f"  {_icon(result)} {name}")
                if result.formatted_data:
                    indented = "\n   ".join(result.formatted_data.split("\n"))
                    lines.append(f"   {indented}")

        return "\n".join(lines)
