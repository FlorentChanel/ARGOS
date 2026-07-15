import json
import re
from dataclasses import dataclass
from enum import StrEnum
from os import name as os_name
from pathlib import Path
from typing import Any

from utils.constants import (
    BANK_EXERCISES_PATH,
    DIFFICULTY_POINTS,
    EXERCISE_FOLDER_PATH,
    EXERCISE_PREFIX,
    METADATA_FILE_NAME,
    SYNC_BASE_PATH,
    TEST_BINARY_SUFFIX,
    UNIT_TESTS_FOLDER_PATH,
    WINDOWS_BINARY_SUFFIX,
)

_FULLNAME_RE = re.compile(rf"^{EXERCISE_PREFIX}(\d+)_(.+)$")


class ExerciseLanguage(StrEnum):
    """Represents the programming language of an exercise."""

    C = "c"
    CPP = "cpp"


class ExerciseDifficulty(StrEnum):
    """Represents the difficulty level of an exercise."""

    EASY = "easy"
    MEDIUM = "medium"
    HARD = "hard"


@dataclass(frozen=True)
class ExerciseMetadata:
    """Metadata loaded from an exercise's metadata.json file."""

    exercise_name: str
    description: str
    difficulty: ExerciseDifficulty
    language: ExerciseLanguage
    skills: list[str]

    @property
    def points(self) -> int:
        return DIFFICULTY_POINTS.get(self.difficulty.value, 1)

    @staticmethod
    def from_json(data: dict[str, Any]) -> "ExerciseMetadata":
        difficulty_str = str(data.get("difficulty", "easy")).lower()
        language_str = str(data.get("language", "")).lower()
        try:
            difficulty = ExerciseDifficulty(difficulty_str)
        except ValueError as error:
            raise ValueError(
                f"Invalid difficulty value: {difficulty_str}. Expected one of: {[d.value for d in ExerciseDifficulty]}"
            ) from error

        try:
            language = ExerciseLanguage(language_str)
        except ValueError as error:
            raise ValueError(
                f"Invalid language value: {language_str}. Expected one of: {[l.value for l in ExerciseLanguage]}"
            ) from error

        return ExerciseMetadata(
            exercise_name=str(data.get("name", "")),
            description=str(data.get("description", "")),
            difficulty=difficulty,
            language=language,
            skills=list(data.get("skills", [])),
        )

    @staticmethod
    def from_exercise(exercise_fullname: str) -> "ExerciseMetadata | None":
        full_path = Path(BANK_EXERCISES_PATH) / exercise_fullname / METADATA_FILE_NAME
        if not full_path.exists():
            return None

        try:
            data: dict[str, Any] = json.loads(full_path.read_text(encoding="utf-8"))
            return ExerciseMetadata.from_json(data)
        except (OSError, json.JSONDecodeError):
            return None

    @staticmethod
    def default() -> "ExerciseMetadata":
        return ExerciseMetadata(
            exercise_name="",
            description="",
            difficulty=ExerciseDifficulty.EASY,
            language=ExerciseLanguage.C,
            skills=[],
        )


@dataclass()
class Exercise:
    """Represents an exercise living on disk."""

    fullname: str
    id: str
    name: str
    test_target_name: str
    test_target_exe_name: str
    main_target_name: str
    bank_exercise_path: Path
    unit_test_path: Path
    root_path: Path
    base_path: Path
    metadata: ExerciseMetadata

    @property
    def points(self) -> int:
        return self.metadata.points

    def __init__(self, fullname: str):
        self.fullname = fullname
        self._parse_fullname()
        self._parse_targets()

        self.bank_exercise_path = Path(BANK_EXERCISES_PATH) / fullname
        self.unit_test_path = Path(UNIT_TESTS_FOLDER_PATH) / fullname
        self.root_path = Path(EXERCISE_FOLDER_PATH) / fullname
        self.base_path = Path(SYNC_BASE_PATH) / fullname

        self.metadata = (
            ExerciseMetadata.from_exercise(fullname) or ExerciseMetadata.default()
        )

    def _parse_fullname(self) -> None:
        match = _FULLNAME_RE.match(self.fullname)
        if not match:
            raise ValueError(
                f"Invalid exercise fullname: {self.fullname!r}, expected format: ex_NNNN_Name"
            )
        self.id = match.group(1).zfill(4)
        self.name = match.group(2)

    def _parse_targets(self) -> None:
        self.main_target_name = f"{EXERCISE_PREFIX}{self.id}"
        self.test_target_name = f"{EXERCISE_PREFIX}{self.id}{TEST_BINARY_SUFFIX}"
        self.test_target_exe_name = self.test_target_name
        # Add .exe on windows
        if os_name == "nt":
            self.test_target_exe_name += WINDOWS_BINARY_SUFFIX
