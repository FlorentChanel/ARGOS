from logging import getLogger

from config.models import ExerciseScope
from tests.google_test_runner import GoogleTestRunner
from utils.constants import ARGOS_FOLDER_NAME, BUILD_FOLDER_NAME

from .models import StepResult, UnitTestsPayload
from .step import PipelineStep

logger = getLogger(__name__)


class UnitTestsStep(PipelineStep[UnitTestsPayload]):
    def __init__(self, google_test_runner: GoogleTestRunner) -> None:
        self._google_test_runner = google_test_runner

    def run(self, scope: ExerciseScope) -> StepResult[UnitTestsPayload]:
        if len(scope.exercises) != 1:
            raise ValueError(
                f"UnitTestsStep expects exactly one exercise in scope, got {len(scope.exercises)}."
            )

        exercise = scope.exercises[0]
        build = scope.root / ARGOS_FOLDER_NAME / BUILD_FOLDER_NAME
        try:
            suite = self._google_test_runner.run(exercise, build)
        except Exception as e:
            logger.error("Failed to run unit tests for '%s': %s", exercise.id, e)
            return StepResult(
                success=False,
                skipped=False,
                formatted_data=f"Unit tests failed to run: {e}",
                data=UnitTestsPayload(),
            )

        return StepResult(
            success=suite.failed_tests == 0,
            skipped=False,
            formatted_data=str(suite),
            data=UnitTestsPayload(suite=suite),
        )
