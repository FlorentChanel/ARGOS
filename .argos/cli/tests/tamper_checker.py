import logging
from pathlib import Path

from config.models import Exercise
from utils.constants import ARGOS_FOLDER_NAME, UNIT_TESTS_FOLDER_NAME
from utils.exercise_utils import ExerciseUtils

logger = logging.getLogger(__name__)


class TamperChecker:
    def check(self, student_root: Path, exercises: list[Exercise]) -> dict[str, bool]:
        """Return {exercise_id: tampered} for every exercise."""
        return {ex.id: self._is_tampered(ex, student_root) for ex in exercises}

    def _is_tampered(self, exercise: Exercise, student_root: Path) -> bool:
        ref_dir = exercise.unit_test_path
        if not ref_dir.exists():
            return False

        test_files = list(ref_dir.glob("*_TEST.cpp"))
        if not test_files:
            return False

        ref_file = test_files[0]
        student_file = (
            student_root
            / ARGOS_FOLDER_NAME
            / UNIT_TESTS_FOLDER_NAME
            / exercise.fullname
            / ref_file.name
        )

        if not student_file.exists():
            logger.debug("Tamper detected for %s: student file missing", exercise.id)
            return True

        tampered = not ExerciseUtils.are_files_identical(ref_file, student_file)
        if tampered:
            logger.debug("Tamper detected for %s: file content differs", exercise.id)
        return tampered
