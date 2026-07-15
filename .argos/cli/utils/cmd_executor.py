import subprocess
from dataclasses import dataclass
from logging import getLogger
from shutil import which
from typing import Callable

logger = getLogger(__name__)


@dataclass
class CmdResult:
    stdout: str | None
    stderr: str | None
    returncode: int


class CmdExecutor:
    def __init__(self, cmd: list[str]):
        self.cmd = cmd

    def execute(
        self,
        output_on_error: bool = True,
        output_on_error_predicate: Callable[[int], bool] | None = None,
    ) -> CmdResult:
        """
        Executes the command and returns the result.
        If `output_on_error` is True, it will log the stdout and stderr if the command fails.
        If `output_on_error_predicate` is provided, it will log the stdout and stderr if the predicate returns True for the return code.
        `output_on_error` should be True if you want to use `output_on_error_predicate`, otherwise it will be ignored.
        """
        logger.debug("Executing command: %s", self.cmd)
        result = self._execute_cmd()

        if (
            output_on_error
            and result.returncode != 0
            and (
                output_on_error_predicate is None
                or output_on_error_predicate(result.returncode)
            )
        ):
            logger.error("Command execution failed with result %s", result.returncode)
            logger.error("stdout: %s", result.stdout)
            logger.error("stderr: %s", result.stderr)

        logger.debug("Command execution completed with result %s", result.returncode)
        return result

    def is_program_installed(self) -> bool:
        if not self.cmd:
            logger.error("No command provided to check for installation.")
            return False

        program_name = self.cmd[0]
        is_installed = which(program_name) is not None
        if not is_installed:
            logger.error(
                "Program '%s' is not installed or not found in PATH.", program_name
            )
        return is_installed

    def _execute_cmd(self) -> CmdResult:
        try:
            result = subprocess.run(
                self.cmd,
                check=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
            )
            return CmdResult(
                stdout=result.stdout.decode("utf-8").rstrip(),
                stderr=result.stderr.decode("utf-8").rstrip(),
                returncode=result.returncode,
            )
        except subprocess.CalledProcessError as e:
            return CmdResult(
                stdout=e.stdout.decode("utf-8").rstrip(),
                stderr=e.stderr.decode("utf-8").rstrip(),
                returncode=e.returncode,
            )
