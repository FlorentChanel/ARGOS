from logging import getLogger
from pathlib import Path

from compilation import NinjaRunner
from config.models import Exercise, ExerciseScope
from utils.constants import ARGOS_FOLDER_NAME, BUILD_FOLDER_NAME

from .models import NinjaPayload, StepResult
from .step import PipelineStep

logger = getLogger(__name__)


class NinjaStep(PipelineStep[NinjaPayload]):
    def __init__(self, ninja_runner: NinjaRunner) -> None:
        self._ninja_runner = ninja_runner

    def run(self, scope: ExerciseScope) -> StepResult[NinjaPayload]:
        if len(scope.exercises) != 1:
            raise ValueError(
                f"NinjaStep expects exactly one exercise in scope, got {len(scope.exercises)}."
            )

        exercise = scope.exercises[0]
        build = scope.root / ARGOS_FOLDER_NAME / BUILD_FOLDER_NAME

        if self._ninja_runner.check_is_up_to_date(exercise.test_target_name, build):
            logger.info("'%s' is already up to date.", exercise.test_target_name)
            return StepResult(
                success=True,
                skipped=True,
                formatted_data=f"{exercise.id}: already up to date.",
                data=NinjaPayload(),
            )

        # We first build the main target to ensure that the main code compiles before attempting to build the test target.
        # This makes the error messages more meaningful, as they will point to issues in the main code rather than the test code.
        success, output = self._build_main_target(exercise, build)
        if not success:
            return StepResult(
                success=False,
                skipped=False,
                formatted_data=f"{exercise.id}: compilation failed.",
                data=NinjaPayload(compilation_output=output),
            )

        success, output = self._build_test_target(exercise, build)
        if not success:
            return StepResult(
                success=False,
                skipped=False,
                formatted_data=f"{exercise.id}: tests compilation failed.",
                data=NinjaPayload(compilation_output=output),
            )

        return StepResult(
            success=True,
            skipped=False,
            formatted_data=f"{exercise.id}: compiled successfully.",
            data=NinjaPayload(compilation_output=output),
        )

    def _build_test_target(self, exercise: Exercise, build: Path) -> tuple[bool, str]:
        success, output = self._ninja_runner.build(exercise.test_target_name, build)
        return success, output

    def _build_main_target(self, exercise: Exercise, build: Path) -> tuple[bool, str]:
        success, output = self._ninja_runner.build(exercise.main_target_name, build)
        return success, output
