import io
import logging
import os
import sys
from logging.handlers import RotatingFileHandler

from admin import (
    ClassManager,
    Evaluation,
    ExerciseBankManager,
    ExerciseSearch,
    MultipleProjectRunner,
    Publisher,
    RepositorySynchronizer,
    SolutionStripper,
    StructureChecker,
)
from admin_dashboard_generator import AdminDashboardGenerator
from commands import (
    AdminCommand,
    CheckCommand,
    Command,
    CommandDispatcher,
    GenerateExeCommand,
    LearningPathCommand,
    SyncCommand,
    VersionCommand,
)
from compilation import CMakeRunner, NinjaRunner
from config import ArgosConfig, Context, LearningPathsManager, WorkspaceSynchronizer
from dashboard_generator import DashboardGenerator
from git_bindings import GitBindings
from pipeline import CMakeStep, NinjaStep, ProcessPipeline, UnitTestsStep
from scoring import ScoreCalculator
from tests import GoogleTestRunner, ResultParser
from utils.constants import ARGOS_FOLDER, HOOKS_FOLDER_PATH, LOG_FILE_PATH, LOG_LEVEL
from utils.logging import ColorFormatter, PlainFormatter

# Fixes encoding error on some Windows Git tools (like in IDE git integrations)
if isinstance(sys.stdout, io.TextIOWrapper):
    sys.stdout.reconfigure(encoding="utf-8")  # pyright: ignore[reportUnknownMemberType]
if isinstance(sys.stderr, io.TextIOWrapper):
    sys.stderr.reconfigure(encoding="utf-8")  # pyright: ignore[reportUnknownMemberType]


def _config_logger() -> logging.Logger:
    os.makedirs(ARGOS_FOLDER, exist_ok=True)

    file_handler = RotatingFileHandler(LOG_FILE_PATH, maxBytes=5_000_000, backupCount=2)
    file_handler.setFormatter(
        PlainFormatter(
            fmt="%(asctime)s  %(levelname)-8s  %(location)s  %(message)s",
            datefmt="%H:%M:%S",
        )
    )

    stderr_handler = logging.StreamHandler()
    stderr_handler.setLevel(logging.WARNING)
    stderr_handler.setFormatter(
        ColorFormatter(
            fmt="%(asctime)s  %(levelname)s  %(location)s  %(message)s",
            datefmt="%H:%M:%S",
        )
    )

    logging.basicConfig(level=LOG_LEVEL, handlers=[file_handler, stderr_handler])

    return logging.getLogger("argo_cli")


def main() -> int:
    logger = _config_logger()

    try:
        # Config
        argos_config = ArgosConfig()
        learning_paths_manager = LearningPathsManager()
        context = Context(learning_paths_manager, argos_config)
        git_bindings = GitBindings()
        workspace_synchronizer = WorkspaceSynchronizer(context, git_bindings)

        # Compilation + tests
        cmake_runner = CMakeRunner()
        ninja_runner = NinjaRunner()
        result_parser = ResultParser()
        google_test_runner = GoogleTestRunner(result_parser)

        # Pipeline
        pipeline = ProcessPipeline(
            CMakeStep(cmake_runner),
            NinjaStep(ninja_runner),
            UnitTestsStep(google_test_runner),
        )

        # Scoring + dashboard
        score_calculator = ScoreCalculator()
        dashboard_generator = DashboardGenerator(git_bindings)
        admin_dashboard_generator = AdminDashboardGenerator()

        # Admin
        repository_synchronizer = RepositorySynchronizer(
            git_bindings, learning_paths_manager
        )
        multiple_project_runner = MultipleProjectRunner(pipeline)
        solution_stripper = SolutionStripper()
        evaluation = Evaluation(
            multiple_project_runner, score_calculator, repository_synchronizer
        )
        exercise_bank_manager = ExerciseBankManager(git_bindings)
        exercise_search = ExerciseSearch()
        class_manager = ClassManager(git_bindings, learning_paths_manager)
        publisher = Publisher(solution_stripper)
        structure_checker = StructureChecker(solution_stripper)

        # Commands
        commands: dict[str, Command] = {
            "learning-path": LearningPathCommand(
                argos_config, learning_paths_manager, workspace_synchronizer
            ),
            "check": CheckCommand(
                context, argos_config, pipeline, score_calculator, dashboard_generator
            ),
            "sync": SyncCommand(workspace_synchronizer),
            "admin": AdminCommand(
                context,
                evaluation,
                solution_stripper,
                learning_paths_manager,
                exercise_bank_manager,
                admin_dashboard_generator,
                exercise_search,
                class_manager,
                publisher,
                structure_checker,
            ),
            "generate-exe": GenerateExeCommand(),
            "version": VersionCommand(),
        }
        dispatcher = CommandDispatcher(commands)
    except Exception as e:
        logger.error("Failed to initialize ARGOS CLI context: %s", e)
        return 1

    if git_bindings.get_hooks_dir() != HOOKS_FOLDER_PATH:
        logger.warning("No Git hooks dir set setting it now")
        git_bindings.set_hooks_dir(HOOKS_FOLDER_PATH)

    return dispatcher.dispatch()


if __name__ == "__main__":
    sys.exit(main())
