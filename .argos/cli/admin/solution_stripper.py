from io import TextIOWrapper
from logging import getLogger
from pathlib import Path
from typing import ClassVar

from utils.constants import (
    BANK_EXERCISES_PATH,
    POSSIBLE_EXERCISE_EXTENSIONS,
    SECTION_BEGIN_TEMPLATE,
    SECTION_END_TEMPLATE,
    SOLUTION_SECTION_NAME,
    TODO_SECTION_NAME,
)

logger = getLogger(__name__)


class SolutionStripper:
    _section_begin: ClassVar[str] = SECTION_BEGIN_TEMPLATE.format(
        name=SOLUTION_SECTION_NAME
    )
    _section_end: ClassVar[str] = SECTION_END_TEMPLATE.format(
        name=SOLUTION_SECTION_NAME
    )
    _todo_begin: ClassVar[str] = SECTION_BEGIN_TEMPLATE.format(name=TODO_SECTION_NAME)
    _todo_end: ClassVar[str] = SECTION_END_TEMPLATE.format(name=TODO_SECTION_NAME)

    def strip_solutions(self, exercise_fullnames: list[str]) -> None:
        for exercise_id in exercise_fullnames:
            self._strip_exercise_solutions(exercise_id)

    def detect_solutions(self, exercise_fullnames: list[str]) -> list[Path]:
        """Returns paths of exercise files that still contain solution blocks."""
        found: list[Path] = []
        for fullname in exercise_fullnames:
            path = self._find_exercise_file(fullname)
            if path is not None and self._has_solution(path):
                found.append(path)
        return found

    def _find_exercise_file(self, exercise_fullname: str) -> Path | None:
        folder_path = Path(BANK_EXERCISES_PATH) / exercise_fullname
        if not folder_path.exists():
            return None
        for extension in POSSIBLE_EXERCISE_EXTENSIONS:
            candidate = (folder_path / exercise_fullname).with_suffix(extension)
            if candidate.exists():
                return candidate
        return None

    def _has_solution(self, file_path: Path) -> bool:
        with open(file_path, encoding="utf-8") as f:
            for line in f:
                if line.strip().upper().startswith(self._section_begin):
                    return True
        return False

    def _strip_exercise_solutions(self, exercise_fullname: str) -> None:
        file_path = self._find_exercise_file(exercise_fullname)

        if file_path is None:
            raise ValueError(
                f"Exercise file {exercise_fullname} not found in the bank."
            )

        with open(file_path, "r") as f:
            content = self._get_content_without_solution(f)

        with open(file_path, "w") as f:
            f.write(content)

        logger.info("Stripped solution from '%s'", exercise_fullname)

    def _get_content_without_solution(self, file: TextIOWrapper) -> str:
        return self.strip_string("".join(file))

    def strip_string(self, content: str) -> str:
        """Removes every solution block (markers included) from the given text."""
        result: list[str] = []
        inside = False

        for line in content.splitlines(keepends=True):
            stripped = line.strip()
            if stripped.upper().startswith(self._section_begin):
                inside = True
            elif stripped.upper().startswith(self._section_end):
                inside = False
            elif not inside:
                result.append(line)

        return "".join(result)

    def count_markers(self, content: str) -> tuple[int, int]:
        """Returns (begin_count, end_count) of solution markers in the given text."""
        begins = ends = 0
        for line in content.splitlines():
            stripped = line.strip().upper()
            if stripped.startswith(self._section_begin):
                begins += 1
            elif stripped.startswith(self._section_end):
                ends += 1
        return begins, ends
