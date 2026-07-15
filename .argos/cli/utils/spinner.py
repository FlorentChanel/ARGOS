# This was AI Generated using claude-code with Sonnet 4.6 model
import sys
import threading
from types import TracebackType

_FRAMES = "⠋⠙⠹⠸⠼⠴⠦⠧⠇⠏"


class Spinner:
    """Animated terminal spinner that runs in a background thread."""

    def __init__(self, message: str = "Running...") -> None:
        self._message = message
        self._stop = threading.Event()
        self._thread = threading.Thread(target=self._spin, daemon=True)
        self._tty = sys.stdout.isatty()

    def _spin(self) -> None:
        i = 0
        while not self._stop.wait(0.1):
            frame = _FRAMES[i % len(_FRAMES)]
            sys.stdout.write(f"\r{frame} {self._message}")
            sys.stdout.flush()
            i += 1

    def __enter__(self) -> "Spinner":
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
            sys.stdout.write("\r" + " " * (len(self._message) + 3) + "\r")
            sys.stdout.flush()
