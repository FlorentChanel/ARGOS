from logging import getLogger
from os import environ
from pathlib import Path

from utils.cmd_executor import CmdExecutor

logger = getLogger(__name__)

_NOTHING_TO_DO = "ninja: no work to do"


class NinjaRunner:
    _command_name = "ninja"
    _build_folder_arg = "-C"

    def check_is_up_to_date(self, target: str | None, build_path: Path) -> bool:
        """Returns True when a dry run shows nothing needs rebuilding for the given target."""
        cmd = [self._command_name, "-n", self._build_folder_arg, str(build_path)]
        if target is not None:
            cmd.append(target)
        executor = CmdExecutor(cmd)
        if not executor.is_program_installed():
            return False
        result = executor.execute(output_on_error=False)
        return result.returncode == 0 and _NOTHING_TO_DO in (result.stdout or "")

    def build(self, target: str | None, build_path: Path) -> tuple[bool, str]:
        cmd = [self._command_name, self._build_folder_arg, str(build_path)]
        if target is not None:
            cmd.append(target)

        logger.debug(
            "Running Ninja build%s", f" for target '{target}'" if target else ""
        )
        executor = CmdExecutor(cmd)
        if not executor.is_program_installed():
            logger.error("Ninja is not installed. Please install Ninja to proceed.")
            return False, ""

        environ["CLICOLOR_FORCE"] = "1"
        result = executor.execute(output_on_error=False)
        output = result.stdout or ""
        if result.returncode != 0:
            logger.error("Failed to build with Ninja.")
            return False, output

        logger.info("Build completed successfully with Ninja.")
        return True, output
