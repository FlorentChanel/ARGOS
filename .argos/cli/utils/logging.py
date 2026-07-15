import logging

_GREY = "\033[90m"
_CYAN = "\033[36m"
_GREEN = "\033[32m"
_YELLOW = "\033[33m"
_RED = "\033[31m"
_BOLD_RED = "\033[1;31m"
_RESET = "\033[0m"

_LEVEL_COLORS = {
    logging.DEBUG: _CYAN,
    logging.INFO: _GREEN,
    logging.WARNING: _YELLOW,
    logging.ERROR: _RED,
    logging.CRITICAL: _BOLD_RED,
}


class PlainFormatter(logging.Formatter):
    def format(self, record: logging.LogRecord) -> str:
        record.location = record.name
        return super().format(record)


class ColorFormatter(logging.Formatter):
    def format(self, record: logging.LogRecord) -> str:
        color = _LEVEL_COLORS.get(record.levelno, _RESET)
        original_levelname = record.levelname
        record.levelname = f"{color}{record.levelname:<8}{_RESET}"
        record.location = f"{_GREY}{record.name}{_RESET}"
        result = super().format(record)
        record.levelname = original_levelname
        return result
