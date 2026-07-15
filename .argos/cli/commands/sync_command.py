from argparse import ArgumentParser
from logging import getLogger

from config import WorkspaceSynchronizer
from utils.output import Output
from utils.spinner import Spinner

from .command import Command

logger = getLogger(__name__)


class SyncCommand(Command):
    help = "Sync the local exercises and unit tests with the exercise bank."

    def __init__(self, workspace_synchronizer: WorkspaceSynchronizer) -> None:
        self._workspace_synchronizer = workspace_synchronizer

    def configure(self, parser: ArgumentParser) -> None:
        parser.description = """Sync the local exercises and unit tests with the exercise bank.
       This command should be run after updating the repository to the latest upstream version"""
        parser.add_argument(
            "--force",
            action="store_true",
            help="Force synchronization even if the repository has uncommitted changes.",
        )
        parser.add_argument(
            "--override",
            action="store_true",
            help="Override all exercises with the versions from exercise bank, even if they where modified locally. Also overrides the locally stored baseline for the exercises.",
        )

    def execute(self, args: dict[str, str]) -> int:
        force = args.get("force", False)
        if not force and self._workspace_synchronizer.has_uncommitted_changes():
            Output.error(
                "There are uncommitted changes in the repository. Please commit or stash them before running this command, or use the --force flag to force synchronization.",
                False,
            )
            return 1

        override = args.get("override", False)
        if override:
            Output.hint(
                "Overriding all exercises with the versions from the exercise bank. This will discard all local changes to the exercises. Use with caution."
            )
            with Spinner("Overriding..."):
                self._workspace_synchronizer.override_all()

            return 0

        with Spinner("Synchronizing..."):
            self._workspace_synchronizer.synchronize()

        Output.success("Synchronization completed successfully.")
        return 0
