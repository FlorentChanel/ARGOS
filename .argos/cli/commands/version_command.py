from argparse import ArgumentParser

from utils.constants import CLI_VERSION_STRING

from .command import Command


class VersionCommand(Command):
    help = "Print the argos CLI version."

    def configure(self, parser: ArgumentParser) -> None:
        pass

    def execute(self, args: dict[str, str]) -> int:
        print(CLI_VERSION_STRING)  # noqa: T201
        return 0
