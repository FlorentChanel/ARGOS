from argparse import ArgumentParser
from logging import getLogger
from pathlib import Path

from config import Context
from config.argos_config import ArgosConfig
from dashboard_generator import DashboardGenerator
from pipeline import ProcessPipeline
from scoring import ScoreCalculator
from utils.constants import DASHBOARD_DATA_FILE_PATH, DASHBOARD_INDEX_FILE_PATH
from utils.output import Output
from utils.spinner import Spinner

from .command import Command

logger = getLogger(__name__)


class CheckCommand(Command):
    help = "Check for the validity of the exercises."

    def __init__(
        self,
        context: Context,
        argos_config: ArgosConfig,
        pipeline: ProcessPipeline,
        score_calculator: ScoreCalculator,
        dashboard_generator: DashboardGenerator,
    ) -> None:
        self._context = context
        self._argos_config = argos_config
        self._pipeline = pipeline
        self._score_calculator = score_calculator
        self._dashboard_generator = dashboard_generator

    def configure(self, parser: ArgumentParser) -> None:
        parser.add_argument(
            "target",
            nargs="?",
            default=None,
            metavar="EXERCISE_OR_PATH_ID",
            help="Run only on a specific exercise or learning path. Defaults to all selected learning paths.",
        )
        parser.add_argument(
            "--touched",
            action="store_true",
            help="Only check exercises that differ from the exercise bank.",
        )

    def execute(self, args: dict[str, str]) -> int:
        if not self._context.learning_paths:
            Output.error(
                "No learning paths selected. Please select at least one learning path.",
                False,
            )
            return 1

        target = args.get("target")
        touched = args.get("touched", False)
        try:
            if touched and target is None:
                scope = self._context.scope_for_touched_exercises()
            elif target is None:
                scope = self._context.full_scope()
            elif self._context.full_scope().contains(target):
                scope = self._context.scope_for_exercise(target)
            else:
                scope = self._context.scope_for_learning_path(target)
        except ValueError as e:
            Output.error(str(e), False)
            return 1

        if len(scope.exercises) == 0:
            Output.success("No exercises to check in the selected scope.")
            return 0

        with Spinner("Running checks..."):
            report = self._pipeline.run(scope)

        summary = self._score_calculator.compute(report, scope)
        print(summary.to_str())

        self._dashboard_generator.generate(
            summary, Path(DASHBOARD_DATA_FILE_PATH), self._context.learning_paths
        )
        print("\n")
        Output.path("Dashboard (ctrl+click to open)", Path(DASHBOARD_INDEX_FILE_PATH))

        return 0 if report.overall_success else 1
