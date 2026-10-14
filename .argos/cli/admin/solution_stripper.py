from collections.abc import Iterator
from logging import getLogger
from pathlib import Path
from typing import ClassVar

from utils.constants import (
    BANK_EXERCISES_PATH,
    SECTION_BEGIN_TEMPLATE,
    SECTION_END_TEMPLATE,
    SOLUTION_SECTION_NAME,
    TEXT_EXTENSIONS,
)

logger = getLogger(__name__)


class SolutionStripper:
    _section_begin: ClassVar[str] = SECTION_BEGIN_TEMPLATE.format(
        name=SOLUTION_SECTION_NAME
    )
    _section_end: ClassVar[str] = SECTION_END_TEMPLATE.format(
        name=SOLUTION_SECTION_NAME
    )

    def strip_solutions(self, exercise_fullnames: list[str]) -> None:
        for exercise_id in exercise_fullnames:
            self._strip_exercise_solutions(exercise_id)

    def detect_solutions(self, exercise_fullnames: list[str]) -> list[Path]:
        """Returns paths of exercise files that still contain solution blocks.

        Every text file of the exercise folder is inspected: a solution can
        live in the header (regime B), the sandbox main or a README, not only
        in the main source file.
        """
        found: list[Path] = []
        for fullname in exercise_fullnames:
            for path in self._iter_exercise_text_files(fullname):
                if self._has_solution(path):
                    found.append(path)
        return found

    def _iter_exercise_text_files(self, exercise_fullname: str) -> Iterator[Path]:
        folder_path = Path(BANK_EXERCISES_PATH) / exercise_fullname
        if not folder_path.exists():
            return
        for path in sorted(folder_path.iterdir()):
            if path.is_file() and path.suffix in TEXT_EXTENSIONS:
                yield path

    def _has_solution(self, file_path: Path) -> bool:
        with open(file_path, encoding="utf-8") as f:
            for line in f:
                if line.strip().upper().startswith(self._section_begin):
                    return True
        return False

    def _strip_exercise_solutions(self, exercise_fullname: str) -> None:
        files = list(self._iter_exercise_text_files(exercise_fullname))

        if not files:
            raise ValueError(
                f"Exercise file {exercise_fullname} not found in the bank."
            )

        for file_path in files:
            with open(file_path, "r", encoding="utf-8", newline="") as f:
                content = f.read()

            stripped = self.strip_string(content)
            if stripped == content:
                continue

            with open(file_path, "w", encoding="utf-8", newline="") as f:
                f.write(stripped)

            logger.info("Stripped solution from '%s'", file_path)

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
