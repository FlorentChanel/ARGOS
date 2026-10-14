from logging import getLogger
from os import environ, remove
from pathlib import Path
from tempfile import NamedTemporaryFile

from config.models import Exercise
from utils.cmd_executor import CmdExecutor
from utils.constants import (
    GTEST_OUTPUT_ENV_VAR,
)

from .models import TestSuite
from .result_parser import ResultParser

logger = getLogger(__name__)


class GoogleTestRunner:
    """
    Runs Google Test unit tests and captures their output in a temporary file. then handles parsing it's content using ResultParser
    """

    def __init__(self, result_parser: ResultParser):
        self._result_parser = result_parser

    def run(self, exercise: Exercise, build_path: Path) -> TestSuite:
        return self._run_exercise(exercise, build_path)

    def _run_exercise(self, exercise: Exercise, build_path: Path) -> TestSuite:
        exercise_path = build_path / exercise.fullname
        if not exercise_path.exists():
            raise ValueError(
                f"Exercise '{exercise}' does not exist in the build folder"
            )

        binary_path = exercise_path / exercise.test_target_exe_name
        if not binary_path.exists():
            raise ValueError(
                f"Test binary for exercise '{exercise}' does not exist. Expected at '{binary_path}'"
            )

        # delete=False + explicit close needed on Windows: NamedTemporaryFile holds an
        # exclusive lock while open, preventing the test binary from writing to it.
        with NamedTemporaryFile(delete=False, suffix=".xml") as temp_file:
            temp_path = temp_file.name

        try:
            environ["GTEST_COLOR"] = "yes"
            environ[GTEST_OUTPUT_ENV_VAR] = f"xml:{temp_path}"
            # Run from the exercise build folder so tests can open their
            # stdin fixtures (*_inputs.txt, shipped there by CMake) by name.
            result = CmdExecutor(
                [str(binary_path)], cwd=str(exercise_path)
            ).execute(output_on_error=False)

            with open(temp_path, encoding="utf-8") as f:
                file_content = f.read()

            if file_content.strip() == "":
                raise ValueError(
                    f"Test binary for exercise '{exercise}' did not produce any output. Please check if the tests are running correctly."
                )

            suite = self._result_parser.parse(file_content)
            return suite.__class__(
                name=suite.name,
                total_tests=suite.total_tests,
                failed_tests=suite.failed_tests,
                test_cases=suite.test_cases,
                output=result.stdout,
            )
        finally:
            if Path(temp_path).exists():
                remove(temp_path)
