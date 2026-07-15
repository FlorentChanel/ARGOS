from logging import getLogger
from pathlib import Path

from utils.cmd_executor import CmdExecutor

logger = getLogger(__name__)


class CMakeRunner:
    """
    Class responsible for running CMake commands to generate build files.
    """

    _command_name = "cmake"
    _source_arg = "-S"
    _build_arg = "-B"
    _generator_arg = "-G"
    _additional_args = [
        "-DCMAKE_BUILD_TYPE=Debug",
        "-DCMAKE_COLOR_DIAGNOSTICS=ON",
    ]

    def generate_build_files(self, src_path: Path, build_path: Path) -> bool:
        cmd = [
            self._command_name,
            self._source_arg,
            str(src_path),
            self._build_arg,
            str(build_path),
            self._generator_arg,
            "Ninja",
        ] + self._additional_args

        logger.debug("Running CMake")
        executor = CmdExecutor(cmd)
        if not executor.is_program_installed():
            logger.error("CMake is not installed. Please install CMake to proceed.")
            return False

        result = executor.execute()
        if result.returncode != 0:
            logger.error("Failed to generate build files with CMake.")
            return False

        logger.info("Build files generated successfully with CMake.")
        return True
