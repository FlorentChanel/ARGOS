from argparse import ArgumentParser
from logging import getLogger
from typing import cast

from config import ArgosConfig, LearningPathsManager, WorkspaceSynchronizer
from config.models import LearningPath
from utils.output import Output

from .command import Command

logger = getLogger(__name__)


class LearningPathCommand(Command):
    help = "Manage the learning paths selection."

    def __init__(
        self,
        argos_config: ArgosConfig,
        learning_paths_manager: LearningPathsManager,
        workspace_synchronizer: WorkspaceSynchronizer,
    ) -> None:
        self._argos_config = argos_config
        self._learning_paths_manager = learning_paths_manager
        self._workspace_synchronizer = workspace_synchronizer

    def configure(self, parser: ArgumentParser) -> None:
        subparsers = parser.add_subparsers(dest="action", required=True)

        add_parser = subparsers.add_parser(
            "add", help="Add a learning path to the selection"
        )
        add_parser.add_argument("id", help="ID of the learning path to add")

        remove_parser = subparsers.add_parser(
            "remove", help="Remove a learning path from the selection"
        )
        remove_parser.add_argument("id", help="ID of the learning path to remove")

        subparsers.add_parser(
            "list", help="List all possible learning paths and the current selection"
        )

    def execute(self, args: dict[str, str]) -> int:
        action = args.get("action")
        id = args.get("id")

        if id is None and action in ["add", "remove"]:
            Output.error("Learning path ID is required.")
            return 1

        match action:
            case "add":
                id = cast(str, id)
                if self._learning_paths_manager.get_learning_path(id) is None:
                    Output.error(
                        f"Learning path '{id}' not found.", show_log_link=False
                    )
                    Output.hint(self._generate_learning_path_not_found_hint(id))
                    return 1
                if id in self._argos_config.learning_paths:
                    Output.warn(f"Learning path '{id}' is already in the selection.")
                    return 1
                self._argos_config.add_learning_path(id)
                Output.success(f"Added learning path '{id}'.")

            case "remove":
                id = cast(str, id)
                if id not in self._argos_config.learning_paths:
                    Output.error(f"Learning path '{id}' is not in the selection.")
                    return 1
                self._argos_config.remove_learning_path(id)
                Output.success(f"Removed learning path '{id}'.")
            case "list":
                learning_paths = self._learning_paths_manager.get_learning_paths()
                selected_learning_paths = self._argos_config.learning_paths

                display_data: list[str] = []
                for learning_path in learning_paths:
                    selected_marker = (
                        "[X]" if learning_path.id in selected_learning_paths else "[ ]"
                    )
                    display_data.append(f"{selected_marker} {learning_path.id}")

                print("\n".join(display_data))
            case _:
                Output.error(f"Unknown action '{action}'.")
                return 1

        if action in ["add", "remove"]:
            self._workspace_synchronizer.synchronize()
        return 0

    def _generate_learning_path_not_found_hint(self, id: str) -> str:
        possible_id: LearningPath | None = None
        if " " in id:
            possible_id = next(
                filter(
                    lambda lp: lp.name == id,
                    self._learning_paths_manager.get_learning_paths(),
                ),
                None,
            )

        if possible_id:
            return f"Did you mean '{possible_id.id}'?\n Learning path IDs are based on the JSON filename not the `name` field in the JSON file."
        return "You can list all available learning paths using the `learning-path list` command."
