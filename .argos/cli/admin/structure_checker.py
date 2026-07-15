import json
import re
from dataclasses import dataclass
from logging import getLogger
from pathlib import Path
from typing import Any

from admin.solution_stripper import SolutionStripper
from config.models import ExerciseDifficulty, ExerciseLanguage
from utils.constants import (
    BANK_EXERCISES_PATH,
    DIFFICULTY_LABELS_FILE_NAME,
    METADATA_FILE_NAME,
    SKILLS_LABELS_FILE_NAME,
    TEST_BINARY_SUFFIX,
    TEXT_EXTENSIONS,
    UNIT_TESTS_FOLDER_PATH,
)

logger = getLogger(__name__)

FULLNAME_RE = re.compile(r"^ex_(\d{4})_([A-Z][A-Za-z0-9]*)$")
MAIN_DEFINITION_RE = re.compile(r"^\s*(?:int|void)\s+main\s*\(", re.MULTILINE)

LANGUAGE_EXTENSIONS = {
    ExerciseLanguage.C.value: ".c",
    ExerciseLanguage.CPP.value: ".cpp",
}

# Folders in unitTests/ that are infrastructure, not exercise mirrors.
NON_EXERCISE_TEST_FOLDERS = {"Common"}


@dataclass(frozen=True)
class StructureIssue:
    exercise: str
    message: str


class StructureChecker:
    """Validates that bank exercises conform to the frozen uniform structure.

    This is the guardrail for LLM-based batch generation: naming, required
    files, metadata, test mirror and solution markers are all checked here,
    and the pre-commit hook of the authoring repository calls this through
    `argos admin check-structure`.
    """

    def __init__(
        self,
        solution_stripper: SolutionStripper,
        bank_path: Path | None = None,
        unit_tests_path: Path | None = None,
    ) -> None:
        self._stripper = solution_stripper
        self._bank_path = bank_path or Path(BANK_EXERCISES_PATH)
        self._unit_tests_path = unit_tests_path or Path(UNIT_TESTS_FOLDER_PATH)
        self._skills_labels: dict[str, Any] = {}
        self._difficulty_labels: dict[str, Any] = {}

    def bank_folder_names(self) -> list[str]:
        return sorted(d.name for d in self._bank_path.iterdir() if d.is_dir())

    def check(self, folder_names: list[str] | None = None) -> list[StructureIssue]:
        """Checks the given bank folders (all of them when None).

        Returns the list of found issues, empty when the structure is valid.
        """
        issues: list[StructureIssue] = []
        issues.extend(self._load_labels())

        all_names = self.bank_folder_names()
        scoped_names = all_names if folder_names is None else sorted(folder_names)

        # Uniqueness is global: duplicated ids are reported even in scoped runs.
        issues.extend(self._check_id_uniqueness(all_names))

        for name in scoped_names:
            issues.extend(self._check_exercise(name))

        if folder_names is None:
            issues.extend(self._check_orphan_test_folders(all_names))

        return issues

    def _load_labels(self) -> list[StructureIssue]:
        issues: list[StructureIssue] = []
        self._skills_labels = self._load_label_table(SKILLS_LABELS_FILE_NAME, issues)
        self._difficulty_labels = self._load_label_table(
            DIFFICULTY_LABELS_FILE_NAME, issues
        )
        return issues

    def _load_label_table(
        self, filename: str, issues: list[StructureIssue]
    ) -> dict[str, Any]:
        path = self._bank_path / filename
        if not path.exists():
            issues.append(StructureIssue("bank", f"Label table not found: {path}"))
            return {}
        try:
            return json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as error:
            issues.append(
                StructureIssue("bank", f"Invalid JSON in {filename}: {error}")
            )
            return {}

    def _check_id_uniqueness(self, all_names: list[str]) -> list[StructureIssue]:
        by_id: dict[str, list[str]] = {}
        for name in all_names:
            match = FULLNAME_RE.match(name)
            if match:
                by_id.setdefault(match.group(1), []).append(name)

        return [
            StructureIssue(
                "bank", f"Duplicated exercise id {id}: {', '.join(names)}"
            )
            for id, names in sorted(by_id.items())
            if len(names) > 1
        ]

    def _check_exercise(self, name: str) -> list[StructureIssue]:
        folder = self._bank_path / name
        if not folder.is_dir():
            return [StructureIssue(name, "Exercise folder not found in the bank.")]

        match = FULLNAME_RE.match(name)
        if not match:
            return [
                StructureIssue(
                    name,
                    "Folder name must match ex_NNNN_SlugCamelCase "
                    "(4-digit id, CamelCase slug).",
                )
            ]
        if match.group(1) == "0000":
            return [StructureIssue(name, "Exercise ids start at 0001, not 0000.")]

        issues: list[StructureIssue] = []
        metadata, metadata_issues = self._read_metadata(name, folder)
        issues.extend(metadata_issues)

        extension = self._source_extension(folder, name, metadata)
        issues.extend(self._check_required_files(name, folder, extension))
        issues.extend(self._check_no_main(name, folder, extension))
        issues.extend(self._check_markers(name, folder))
        issues.extend(self._check_test_mirror(name, match.group(1), extension))

        return issues

    def _read_metadata(
        self, name: str, folder: Path
    ) -> tuple[dict[str, Any] | None, list[StructureIssue]]:
        path = folder / METADATA_FILE_NAME
        if not path.exists():
            # The missing file itself is reported by the required-files check.
            return None, []

        try:
            data: dict[str, Any] = json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as error:
            return None, [
                StructureIssue(name, f"Invalid JSON in {METADATA_FILE_NAME}: {error}")
            ]

        return data, self._validate_metadata(name, data)

    def _validate_metadata(
        self, name: str, data: dict[str, Any]
    ) -> list[StructureIssue]:
        issues: list[StructureIssue] = []

        for field in ("name", "description"):
            value = data.get(field)
            if not isinstance(value, str) or not value.strip():
                issues.append(
                    StructureIssue(
                        name, f"metadata.json: '{field}' must be a non-empty string."
                    )
                )

        difficulty = data.get("difficulty")
        allowed_difficulties = [d.value for d in ExerciseDifficulty]
        if difficulty not in allowed_difficulties:
            issues.append(
                StructureIssue(
                    name,
                    f"metadata.json: 'difficulty' must be one of {allowed_difficulties} "
                    f"(got {difficulty!r}).",
                )
            )
        elif self._difficulty_labels and difficulty not in self._difficulty_labels:
            issues.append(
                StructureIssue(
                    name,
                    f"metadata.json: difficulty '{difficulty}' is missing from "
                    f"{DIFFICULTY_LABELS_FILE_NAME}.",
                )
            )

        language = data.get("language")
        allowed_languages = [lang.value for lang in ExerciseLanguage]
        if language not in allowed_languages:
            issues.append(
                StructureIssue(
                    name,
                    f"metadata.json: 'language' must be one of {allowed_languages} "
                    f"(got {language!r}).",
                )
            )

        skills = data.get("skills")
        if not isinstance(skills, list) or not skills:
            issues.append(
                StructureIssue(
                    name, "metadata.json: 'skills' must be a non-empty array of keys."
                )
            )
        else:
            for skill in skills:
                if not isinstance(skill, str):
                    issues.append(
                        StructureIssue(
                            name, f"metadata.json: skill {skill!r} is not a string."
                        )
                    )
                elif self._skills_labels and skill not in self._skills_labels:
                    issues.append(
                        StructureIssue(
                            name,
                            f"metadata.json: skill '{skill}' is missing from "
                            f"{SKILLS_LABELS_FILE_NAME}.",
                        )
                    )

        return issues

    def _source_extension(
        self, folder: Path, name: str, metadata: dict[str, Any] | None
    ) -> str:
        language = (metadata or {}).get("language")
        if isinstance(language, str) and language in LANGUAGE_EXTENSIONS:
            return LANGUAGE_EXTENSIONS[language]
        # Invalid metadata: infer from what exists so file checks stay useful.
        if (folder / f"{name}.cpp").exists():
            return ".cpp"
        return ".c"

    def _check_required_files(
        self, name: str, folder: Path, extension: str
    ) -> list[StructureIssue]:
        required = [
            f"{name}{extension}",
            f"{name}.h",
            METADATA_FILE_NAME,
            "README.en.md",
            "README.fr.md",
        ]
        issues = [
            StructureIssue(name, f"Missing required file: {filename}")
            for filename in required
            if not (folder / filename).is_file()
        ]
        if not any((folder / f"main{ext}").is_file() for ext in (".c", ".cpp")):
            issues.append(StructureIssue(name, "Missing sandbox main.c"))
        return issues

    def _check_no_main(
        self, name: str, folder: Path, extension: str
    ) -> list[StructureIssue]:
        issues: list[StructureIssue] = []
        for filename in (f"{name}{extension}", f"{name}.h"):
            path = folder / filename
            if not path.is_file():
                continue
            content = self._read_text(path)
            if content is not None and MAIN_DEFINITION_RE.search(content):
                issues.append(
                    StructureIssue(
                        name,
                        f"{filename} defines a main() - the student file must never "
                        "contain one (the sandbox main lives in main.c).",
                    )
                )
        return issues

    def _check_markers(self, name: str, folder: Path) -> list[StructureIssue]:
        issues: list[StructureIssue] = []
        test_folder = self._unit_tests_path / name
        files = list(self._iter_text_files(folder)) + list(
            self._iter_text_files(test_folder)
        )
        for path in files:
            content = self._read_text(path)
            if content is None:
                issues.append(StructureIssue(name, f"{path.name} is not valid UTF-8."))
                continue
            begins, ends = self._stripper.count_markers(content)
            if begins != ends:
                issues.append(
                    StructureIssue(
                        name,
                        f"Unbalanced SOLUTION markers in {path.name} "
                        f"({begins} BEGIN / {ends} END).",
                    )
                )
        return issues

    def _check_test_mirror(
        self, name: str, exercise_id: str, extension: str
    ) -> list[StructureIssue]:
        test_folder = self._unit_tests_path / name
        if not test_folder.is_dir():
            return [
                StructureIssue(
                    name, f"Missing unit tests folder: unitTests/{name}/"
                )
            ]

        test_filename = f"ex_{exercise_id}{TEST_BINARY_SUFFIX}.cpp"
        test_path = test_folder / test_filename
        if not test_path.is_file():
            return [
                StructureIssue(
                    name, f"Missing test file: unitTests/{name}/{test_filename}"
                )
            ]

        content = self._read_text(test_path)
        if content is not None and f"{name}{extension}" not in content:
            return [
                StructureIssue(
                    name,
                    f"{test_filename} does not reference the exercise source "
                    f"({name}{extension}).",
                )
            ]
        return []

    def _check_orphan_test_folders(
        self, all_names: list[str]
    ) -> list[StructureIssue]:
        if not self._unit_tests_path.is_dir():
            return [
                StructureIssue(
                    "bank", f"Unit tests folder not found: {self._unit_tests_path}"
                )
            ]
        known = set(all_names)
        return [
            StructureIssue(
                folder.name,
                "Unit tests folder has no matching exercise in the bank.",
            )
            for folder in sorted(self._unit_tests_path.iterdir())
            if folder.is_dir()
            and folder.name not in NON_EXERCISE_TEST_FOLDERS
            and folder.name not in known
        ]

    def _iter_text_files(self, folder: Path) -> list[Path]:
        if not folder.is_dir():
            return []
        return sorted(
            path
            for path in folder.iterdir()
            if path.is_file() and path.suffix in TEXT_EXTENSIONS
        )

    def _read_text(self, path: Path) -> str | None:
        try:
            return path.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError):
            return None
