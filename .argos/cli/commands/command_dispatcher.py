from argparse import ArgumentParser

from utils.constants import CLI_NAME, CLI_VERSION_STRING

from .command import Command


class CommandDispatcher:
    def __init__(self, commands: dict[str, Command]) -> None:
        self._commands = commands

    def dispatch(self) -> int:
        parser = ArgumentParser(prog=CLI_NAME)
        parser.add_argument("--version", action="version", version=CLI_VERSION_STRING)
        subparsers = parser.add_subparsers(dest="command")
        for name, cmd in self._commands.items():
            cmd.configure(subparsers.add_parser(name, help=cmd.help))

        args = parser.parse_args()
        if not args.command:
            parser.print_help()
            return 0

        cmd = self._commands.get(args.command)
        if cmd is None:
            parser.print_help()
            return 0

        return cmd.execute(vars(args))
