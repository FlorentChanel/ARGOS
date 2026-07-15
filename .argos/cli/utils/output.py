# ruff: noqa: T201
import shutil
import sys
import textwrap
from pathlib import Path

from utils.constants import LOG_FILE_PATH, ROOT_FOLDER

_GREEN = "\033[32m"
_CYAN = "\033[36m"
_GREY = "\033[90m"
_RED = "\033[31m"
_BOLD = "\033[1m"
_RESET = "\033[0m"
_YELLOW = "\033[33m"


def _tty() -> bool:
    return sys.stdout.isatty()


def _fmt(msg: str, *codes: str) -> str:
    return f"{''.join(codes)}{msg}{_RESET}" if _tty() else msg


def _link(path: Path, label: str | None = None) -> str:
    path = path.resolve()
    uri = path.as_uri()
    return (
        f"{_CYAN}\033]8;;{uri}\033\\{path.relative_to(ROOT_FOLDER) if label is None else label}\033]8;;\033\\{_RESET}"
        if _tty()
        else str(path)
    )


class Output:
    @staticmethod
    def success(msg: str) -> None:
        print(_fmt(f"✓ {msg}", _BOLD, _GREEN))

    @staticmethod
    def warn(msg: str) -> None:
        print(_fmt(f"⚠️  {msg}", _BOLD, _YELLOW))

    @staticmethod
    def error(msg: str, show_log_link: bool = True) -> None:

        print(_fmt(f"✗ {msg}", _BOLD, _RED))
        if show_log_link:
            print(
                _fmt(f"  See {_link(Path(LOG_FILE_PATH), 'logs')} for details.", _GREY)
            )

    @staticmethod
    def hint(msg: str) -> None:
        print(_fmt(msg, _GREY))

    @staticmethod
    def path(label: str, path: Path | str) -> None:
        print(f"  {label}: {_link(Path(path))}")

    @staticmethod
    def table(
        headers: list[str],
        rows: list[list[str]],
        wrap_col: int | None = None,
        wrap_cols: list[int] | None = None,
    ) -> None:
        effective_wrap_cols: list[int] = (
            wrap_cols
            if wrap_cols is not None
            else ([wrap_col] if wrap_col is not None else [])
        )

        col_widths = [
            max(len(headers[i]), max((len(row[i]) for row in rows), default=0))
            for i in range(len(headers))
        ]

        if effective_wrap_cols:
            terminal_width = shutil.get_terminal_size(fallback=(120, 24)).columns
            n_cols = len(headers)
            overhead = 2 + 5 * (n_cols - 1)  # leading indent + "  │  " separators
            fixed_cols_width = sum(
                w for i, w in enumerate(col_widths) if i not in effective_wrap_cols
            )
            remaining = terminal_width - overhead - fixed_cols_width
            per_wrap = max(20, remaining // len(effective_wrap_cols))
            for i in effective_wrap_cols:
                col_widths[i] = per_wrap

        def fmt_row(cells: list[str], bold: bool = False) -> str:
            padded = "  │  ".join(
                cell.ljust(col_widths[i]) for i, cell in enumerate(cells)
            )
            return _fmt(f"  {padded}", _BOLD) if bold else f"  {padded}"

        def render_row(cells: list[str]) -> list[str]:
            if not effective_wrap_cols:
                return [fmt_row(cells)]
            wrapped_cols = {
                i: textwrap.wrap(cells[i], col_widths[i]) or [""]
                for i in effective_wrap_cols
            }
            n_lines = max(len(lines) for lines in wrapped_cols.values())
            result: list[str] = []
            for k in range(n_lines):
                row_cells = ["" if k > 0 else cells[i] for i in range(len(cells))]
                for i in effective_wrap_cols:
                    lines = wrapped_cols[i]
                    row_cells[i] = lines[k] if k < len(lines) else ""
                result.append(fmt_row(row_cells))
            return result

        separator = "  " + "──┼──".join("─" * w for w in col_widths)

        print(fmt_row(headers, bold=True))
        print(separator)
        for row in rows:
            for line in render_row(row):
                print(line)
            print(separator)
