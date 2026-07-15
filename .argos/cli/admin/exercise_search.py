from pathlib import Path

from config.models import Exercise, ExerciseDifficulty, ExerciseLanguage
from utils.constants import BANK_EXERCISES_PATH, METADATA_FILE_NAME


class ExerciseSearch:
    def __init__(self):
        pass

    def get_exercises(
        self,
        language: ExerciseLanguage,
        difficulty: ExerciseDifficulty | None,
        skills: list[str],
        match_all_skills: bool = True,
    ) -> list[Exercise]:
        exercises: list[Exercise] = []
        for exercise_folder in (Path(BANK_EXERCISES_PATH)).iterdir():
            if not exercise_folder.is_dir():
                continue

            metadata_file = exercise_folder / METADATA_FILE_NAME
            if not metadata_file.exists():
                continue

            try:
                exercise = Exercise(exercise_folder.name)
            except ValueError:
                continue

            metadata = exercise.metadata

            if metadata.language != language:
                continue

            if difficulty is not None and metadata.difficulty != difficulty:
                continue

            if (
                match_all_skills
                and skills
                and not all(skill in metadata.skills for skill in skills)
            ):
                continue

            if (
                not match_all_skills
                and skills
                and not any(skill in metadata.skills for skill in skills)
            ):
                continue

            exercises.append(exercise)

        return exercises
