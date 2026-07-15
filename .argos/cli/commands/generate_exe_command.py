from argparse import ArgumentParser
from logging import getLogger
from os import name as os_name
from os import path

from utils.constants import CLI_FOLDER, CLI_NAME, ROOT_FOLDER
from utils.output import Output
from utils.spinner import Spinner

from .command import Command

logger = getLogger(__name__)


class GenerateExeCommand(Command):
    help = "Generate an windows executable of this CLI."

    def configure(self, parser: ArgumentParser) -> None:
        pass

    def execute(self, args: dict[str, str]) -> int:
        if os_name != "nt":
            Output.error(
                "Executable generation is only supported on Windows.",
                show_log_link=False,
            )
            return 1

        try:
            import PyInstaller.__main__ as pyinstaller

            entry_path = path.join(CLI_FOLDER, "argos_cli.py")

            with Spinner("Generating executable..."):
                pyinstaller.run(
                    [
                        "--onefile",
                        "--nowindow",
                        "--noconfirm",
                        "--name",
                        CLI_NAME,
                        "--distpath",
                        ROOT_FOLDER,
                        entry_path,
                    ]
                )

            with Spinner("Removing build artifacts..."):
                build_path = path.join(ROOT_FOLDER, "build")
                spec_path = path.join(ROOT_FOLDER, f"{CLI_NAME}.spec")
                if path.exists(build_path):
                    import shutil

                    shutil.rmtree(build_path)
                if path.exists(spec_path):
                    import os

                    os.remove(spec_path)

            Output.success("Executable generated successfully.")
            return 0
        except ImportError:
            Output.error(
                "PyInstaller is not installed. Please install it with 'pip install pyinstaller'.",
                show_log_link=False,
            )
            return 1
