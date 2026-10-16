import shutil
import sys
import threading
from types import TracebackType

_FRAMES = "⠋⠙⠹⠸⠼⠴⠦⠧⠇⠏"
_FILLED = "█"
_EMPTY = "░"
_CLEAR_LINE = "\033[K"


class ProgressBar:
    """Single-line terminal progress bar, redrawn from a background thread so
    the spinner keeps moving during long steps."""

    def __init__(self, detail: str = "", bar_width: int = 24) -> None:
        self._bar_width = bar_width
        self._completed = 0
        self._total = 0
        self._detail = detail
        self._lock = threading.Lock()
        self._stop = threading.Event()
        self._thread = threading.Thread(target=self._animate, daemon=True)
        self._tty = sys.stdout.isatty()

    def update(self, completed: int, total: int, detail: str) -> None:
        with self._lock:
            self._completed = completed
            self._total = total
            self._detail = detail

    def _render(self, frame: str) -> str:
        with self._lock:
            completed, total, detail = self._completed, self._total, self._detail

        ratio = completed / total if total else 0.0
        filled = round(ratio * self._bar_width)
        bar = _FILLED * filled + _EMPTY * (self._bar_width - filled)
        line = f"{frame} [{bar}] {ratio:4.0%}  {detail}"

        # A wrapped line cannot be redrawn in place with \r.
        max_width = shutil.get_terminal_size().columns - 1
        return line[:max_width]

    def _animate(self) -> None:
        i = 0
        while not self._stop.wait(0.1):
            sys.stdout.write(f"\r{self._render(_FRAMES[i % len(_FRAMES)])}{_CLEAR_LINE}")
            sys.stdout.flush()
            i += 1

    def __enter__(self) -> "ProgressBar":
        if self._tty:
            self._thread.start()
        return self

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: TracebackType | None,
    ) -> None:
        self._stop.set()
        if self._tty and self._thread.is_alive():
            self._thread.join()
            sys.stdout.write(f"\r{_CLEAR_LINE}")
            sys.stdout.flush()
