from logging import getLogger
from typing import TypeVar

from config.models import ExerciseScope

from .cmake_step import CMakeStep
from .models import (
    ExerciseStepResults,
    NinjaPayload,
    PipelineReport,
    StepName,
    StepResult,
    UnitTestsPayload,
)
from .ninja_step import NinjaStep
from .unit_tests_step import UnitTestsStep

logger = getLogger(__name__)

PayloadT = TypeVar("PayloadT")


def _skipped(missing: list[StepName], payload: PayloadT) -> StepResult[PayloadT]:
    return StepResult(
        success=False,
        skipped=True,
        formatted_data=(
            f"Skipped: required steps {', '.join(missing)} did not succeed."
        ),
        data=payload,
    )


class ProcessPipeline:
    def __init__(
        self,
        cmake_step: CMakeStep,
        ninja_step: NinjaStep,
        unit_tests_step: UnitTestsStep,
    ) -> None:
        self._cmake_step = cmake_step
        self._ninja_step = ninja_step
        self._unit_tests_step = unit_tests_step

    def run(self, scope: ExerciseScope) -> PipelineReport:
        logger.debug("Running global step '%s'.", StepName.CMAKE)
        cmake_result = self._cmake_step.run(scope)

        exercise_results: dict[str, ExerciseStepResults] = {}

        for exercise in scope.exercises:
            ex_scope = ExerciseScope(
                root=scope.root,
                exercises=[exercise],
                series_by_exercise={
                    exercise.id: scope.series_by_exercise.get(exercise.id, [])
                },
            )

            if not cmake_result.success:
                ninja_result = _skipped([StepName.CMAKE], NinjaPayload())
                unit_tests_result = _skipped([StepName.CMAKE], UnitTestsPayload())
            else:
                logger.debug(
                    "Running step '%s' for exercise '%s'.", StepName.NINJA, exercise.id
                )
                ninja_result = self._ninja_step.run(ex_scope)
                if ninja_result.success:
                    logger.debug(
                        "Running step '%s' for exercise '%s'.",
                        StepName.UNIT_TESTS,
                        exercise.id,
                    )
                    unit_tests_result = self._unit_tests_step.run(ex_scope)
                else:
                    unit_tests_result = _skipped([StepName.NINJA], UnitTestsPayload())

            exercise_results[exercise.id] = ExerciseStepResults(
                ninja=ninja_result,
                unit_tests=unit_tests_result,
            )

        return PipelineReport(
            cmake=cmake_result,
            exercise_results=exercise_results,
        )
