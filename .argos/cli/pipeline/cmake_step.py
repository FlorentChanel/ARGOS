from pathlib import Path

from compilation import CMakeRunner
from config.models import ExerciseScope
from utils.constants import ARGOS_FOLDER_NAME, BUILD_FOLDER_NAME, UNIT_TESTS_FOLDER_PATH

from .models import EmptyPayload, StepResult
from .step import PipelineStep


class CMakeStep(PipelineStep[EmptyPayload]):
    def __init__(self, cmake_runner: CMakeRunner) -> None:
        self._cmake_runner = cmake_runner

    def run(self, scope: ExerciseScope) -> StepResult[EmptyPayload]:
        src = Path(UNIT_TESTS_FOLDER_PATH)
        build = scope.root / ARGOS_FOLDER_NAME / BUILD_FOLDER_NAME
        if not self._cmake_runner.generate_build_files(src, build):
            return StepResult(
                success=False,
                skipped=False,
                formatted_data="CMake failed to generate build files.",
                data=EmptyPayload(),
            )
        return StepResult(
            success=True,
            skipped=False,
            formatted_data="Build files generated.",
            data=EmptyPayload(),
        )
