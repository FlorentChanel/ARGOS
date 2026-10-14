import filecmp
from pathlib import Path

from config.models import Exercise

from .constants import COPY_ONLY_EXERCISE_EXTENSIONS, SYNC_MERGE_EXTENSIONS


class ExerciseUtils:
    @staticmethod
    def is_untouched(exercise: Exercise) -> bool:
        """
        Determines if the exercise has been modified by the student.
        An exercise is considered untouched if all source files in the student's workspace
        are identical to those in the bank.
        """
        if not exercise.root_path.exists() or not exercise.bank_exercise_path.exists():
            return True  # If either path doesn't exist, consider it untouched

        for bank_file in exercise.bank_exercise_path.iterdir():
            if not ExerciseUtils.is_source_file(bank_file):
                continue

            student_file = exercise.root_path / bank_file.name
            if not ExerciseUtils.are_files_identical(bank_file, student_file):
                return False  # Found a modified or missing file

        return True  # All source files are identical

    @staticmethod
    def are_files_identical(file1: Path, file2: Path) -> bool:
        """
        Compares two files to determine if they are identical.
        Returns True if the files are identical, False otherwise.
        """
        if not file1.exists() or not file2.exists():
            return False  # If either file doesn't exist, they can't be identical

        return filecmp.cmp(str(file1), str(file2), shallow=False)

    @staticmethod
    def is_source_file(file_path: Path) -> bool:
        """
        Determines if the given file is a student-editable source file (headers
        included) based on its extension.
        """
        return file_path.suffix in SYNC_MERGE_EXTENSIONS

    @staticmethod
    def is_copy_only_file(file_path: Path) -> bool:
        return file_path.suffix in COPY_ONLY_EXERCISE_EXTENSIONS
