from collections.abc import Callable
from logging import getLogger
from typing import TypeVar

from config.models import ExerciseScope

from .cmake_step import CMakeStep
from .models import (
    ExerciseStepResults,
    NinjaPayload,
    PipelineProgress,
    PipelineReport,
    StepName,
    StepResult,
    UnitTestsPayload,
)
from .ninja_step import NinjaStep
from .unit_tests_step import UnitTestsStep

logger = getLogger(__name__)

PayloadT = TypeVar("PayloadT")

ProgressCallback = Callable[[PipelineProgress], None]

_STEPS_PER_EXERCISE = 2


def _skipped(missing: list[StepName], payload: PayloadT) -> StepResult[PayloadT]:
    return StepResult(
        success=False,
        skipped=True,
        formatted_data=(
            f"Skipped: required steps {', '.join(missing)} did not succeed."
        ),
        data=payload,
    )


class _ProgressTracker:
    def __init__(self, exercise_count: int, on_progress: ProgressCallback | None) -> None:
        self._on_progress = on_progress
        self._exercise_count = exercise_count
        self._total_steps = 1 + exercise_count * _STEPS_PER_EXERCISE
        self._completed_steps = 0
        self._exercise_index = 0
        self._passed = 0
        self._failed = 0

    def start(self, step: StepName, exercise_id: str | None = None) -> None:
        self._emit(step, exercise_id)

    def step_done(self) -> None:
        self._completed_steps += 1

    def exercise_done(self, success: bool, skipped_steps: int) -> None:
        self._completed_steps += skipped_steps
        self._exercise_index += 1
        if success:
            self._passed += 1
        else:
            self._failed += 1
        self._emit(None, None)

    def _emit(self, step: StepName | None, exercise_id: str | None) -> None:
        if self._on_progress is None:
            return
        self._on_progress(
            PipelineProgress(
                completed_steps=self._completed_steps,
                total_steps=self._total_steps,
                exercise_index=self._exercise_index + (0 if exercise_id is None else 1),
                exercise_count=self._exercise_count,
                passed=self._passed,
                failed=self._failed,
                current_exercise=exercise_id,
                current_step=step,
            )
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

    def run(
        self, scope: ExerciseScope, on_progress: ProgressCallback | None = None
    ) -> PipelineReport:
        progress = _ProgressTracker(len(scope.exercises), on_progress)

        logger.debug("Running global step '%s'.", StepName.CMAKE)
        progress.start(StepName.CMAKE)
        cmake_result = self._cmake_step.run(scope)
        progress.step_done()

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
                skipped_steps = _STEPS_PER_EXERCISE
            else:
                logger.debug(
                    "Running step '%s' for exercise '%s'.", StepName.NINJA, exercise.id
                )
                progress.start(StepName.NINJA, exercise.id)
                ninja_result = self._ninja_step.run(ex_scope)
                progress.step_done()
                if ninja_result.success:
                    logger.debug(
                        "Running step '%s' for exercise '%s'.",
                        StepName.UNIT_TESTS,
                        exercise.id,
                    )
                    progress.start(StepName.UNIT_TESTS, exercise.id)
                    unit_tests_result = self._unit_tests_step.run(ex_scope)
                    progress.step_done()
                    skipped_steps = 0
                else:
                    unit_tests_result = _skipped([StepName.NINJA], UnitTestsPayload())
                    skipped_steps = 1

            exercise_results[exercise.id] = ExerciseStepResults(
                ninja=ninja_result,
                unit_tests=unit_tests_result,
            )
            progress.exercise_done(unit_tests_result.success, skipped_steps)

        return PipelineReport(
            cmake=cmake_result,
            exercise_results=exercise_results,
        )
