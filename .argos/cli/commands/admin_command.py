import re
from argparse import ArgumentParser
from logging import getLogger
from pathlib import Path

from admin import (
    ClassManager,
    Evaluation,
    ExerciseBankManager,
    ExerciseSearch,
    Publisher,
    PublishError,
    SolutionStripper,
    StructureChecker,
)
from admin_dashboard_generator import AdminDashboardGenerator
from config import Context, LearningPathsManager
from config.models import ExerciseDifficulty, ExerciseLanguage, Student
from utils.constants import (
    ADMIN_DASHBOARD_DATA_FILE_PATH,
    ADMIN_DASHBOARD_INDEX_FILE_PATH,
    BANK_EXERCISES_PATH,
)
from utils.output import Output
from utils.spinner import Spinner

from .command import Command

logger = getLogger(__name__)

REPO_URL_REGEX_FORMAT = re.compile(r"^[a-zA-Z0-9_-]+\/[a-zA-Z0-9_-]+$")
SLUG_REGEX_FORMAT = re.compile(r"^[A-Z][A-Za-z0-9]*$")


class AdminCommand(Command):
    help = "Admin commands for ARGOS. Intended for professors and not students."

    def __init__(
        self,
        context: Context,
        evaluation: Evaluation,
        solution_stripper: SolutionStripper,
        learning_paths_manager: LearningPathsManager,
        exercise_bank_manager: ExerciseBankManager,
        admin_dashboard_generator: AdminDashboardGenerator,
        exercise_search: ExerciseSearch,
        class_manager: ClassManager,
        publisher: Publisher,
        structure_checker: StructureChecker,
    ) -> None:
        self._context = context
        self._evaluation = evaluation
        self._solution_stripper = solution_stripper
        self._learning_paths_manager = learning_paths_manager
        self._exercise_bank_manager = exercise_bank_manager
        self._admin_dashboard_generator = admin_dashboard_generator
        self._exercise_search = exercise_search
        self._class_manager = class_manager
        self._publisher = publisher
        self._structure_checker = structure_checker

    def configure(self, parser: ArgumentParser) -> None:
        parser.description = """Admin commands for ARGOS. This command is intended for professors and not students.
        It can be used to perform administrative tasks such as managing the exercise bank, managing the learning paths, and other tasks that are not related to the students workflow.
        """

        subparsers = parser.add_subparsers(dest="action", required=True)

        create_parser = subparsers.add_parser("create", help="Create ARGOS resources")
        create_subparsers = create_parser.add_subparsers(
            dest="create_action", required=True
        )

        create_lp_parser = create_subparsers.add_parser(
            "learning-path", help="Create a new learning path"
        )
        create_lp_parser.add_argument("id", help="ID of the learning path to create")
        create_lp_parser.add_argument(
            "based_on",
            nargs="?",
            default=None,
            metavar="BASED_ON",
            help="ID of the learning path to use as a template (optional)",
        )

        create_subparsers.add_parser("exercise", help="Create a new exercise")

        create_class_parser = create_subparsers.add_parser(
            "class",
            help="Create a new class file in .argos/classes/ and check that repositories are reachable",
        )
        create_class_parser.add_argument(
            "name", help="Name of the class (becomes the filename)"
        )
        create_class_parser.add_argument(
            "--learning-path",
            required=True,
            metavar="ID",
            help="Learning path ID for this class",
        )
        create_class_parser.add_argument(
            "--from-csv",
            metavar="FILE",
            default=None,
            help="Import students from a CSV file (headers: name, repoUrl)",
        )
        create_class_parser.add_argument(
            "--ssh",
            action="store_true",
            help="Use SSH URLs when checking if repositories are reachable.",
        )
        create_class_parser.add_argument(
            "--skip-repository-check",
            action="store_true",
            help="Skips checking if repositories are reachable",
        )

        eval_parser = subparsers.add_parser(
            "eval", help="Evaluate a class and generate a CSV report"
        )
        eval_parser.add_argument(
            "class_name",
            metavar="CLASS",
            help="Name of the class to evaluate (must exist in .argos/classes/)",
        )
        eval_parser.add_argument(
            "--output",
            default="results.csv",
            metavar="FILE",
            help="Output CSV file path (default: results.csv)",
        )
        eval_parser.add_argument(
            "--ssh",
            action="store_true",
            help="Use SSH URLs for GitHub repositories instead of HTTPS",
        )

        solution_parser = subparsers.add_parser(
            "solution", help="Manage exercise solutions in the bank"
        )
        solution_subparsers = solution_parser.add_subparsers(
            dest="solution_action", required=True
        )

        solution_strip_parser = solution_subparsers.add_parser(
            "strip", help="Strip solution blocks from exercises"
        )
        solution_strip_parser.add_argument(
            "exercises",
            help="Exercise fullnames to strip (comma separated or 'all')",
        )

        solution_detect_parser = solution_subparsers.add_parser(
            "detect",
            help="Detect exercises that still contain solution blocks. Exits with 1 if any are found.",
        )
        solution_detect_parser.add_argument(
            "exercises",
            nargs="?",
            default="all",
            help="Exercise fullnames to check (comma separated or 'all', default: all)",
        )

        search_parser = subparsers.add_parser(
            "search",
            help="Search exercises in the bank by language, difficulty, and skills",
        )
        search_parser.add_argument(
            "--language",
            required=True,
            choices=[lang.value for lang in ExerciseLanguage],
            help="Programming language to filter by",
        )
        search_parser.add_argument(
            "--difficulty",
            choices=[diff.value for diff in ExerciseDifficulty],
            default=None,
            help="Difficulty level to filter by (optional)",
        )
        search_parser.add_argument(
            "--skill",
            dest="skills",
            action="append",
            default=[],
            metavar="SKILL",
            help="Skill to filter by (repeatable, default: match all)",
        )
        search_parser.add_argument(
            "--any",
            dest="match_any",
            action="store_true",
            help="Match exercises that have any of the given skills instead of all",
        )

        check_structure_parser = subparsers.add_parser(
            "check-structure",
            help="Validate that bank exercises conform to the uniform structure. Exits with 1 on any issue.",
        )
        check_structure_parser.description = """Validates the bank against the frozen exercise structure:
        folder naming, id uniqueness, required files, metadata (schema fields + label keys),
        unit-test mirror and balanced SOLUTION markers.
        This is the guardrail called by the authoring pre-commit hook."""
        check_structure_parser.add_argument(
            "exercises",
            nargs="?",
            default="all",
            help="Exercise ids or fullnames to check (comma separated or 'all', default: all)",
        )

        publish_parser = subparsers.add_parser(
            "publish",
            help="Publish stripped exercises to a student repository working copy",
        )
        publish_parser.description = """Publishes the bank to a local working copy of the student repository:
        strips solution blocks, generates the README banners and regenerates the exercise catalogue.
        Never runs git — review the resulting diff, then commit and push manually."""
        publish_parser.add_argument(
            "target",
            metavar="TARGET_DIR",
            help="Path to the local working copy of the student repository",
        )
        publish_parser.add_argument(
            "--exercises",
            default="all",
            metavar="IDS",
            help="Exercise ids or fullnames to publish (comma separated, default: all)",
        )

    def execute(self, args: dict[str, str]) -> int:
        action = args.get("action")
        logger.info("Executing admin command with subcommand '%s'", action)
        match action:
            case "eval":
                return self._evaluate(args)
            case "solution":
                return self._handle_solution(args)
            case "create":
                return self._handle_create(args)
            case "search":
                return self._search_exercises(args)
            case "check-structure":
                return self._check_structure(args)
            case "publish":
                return self._publish(args)
            case _:
                Output.error(f"Unknown admin action '{action}'.")
                return 1

    def _check_structure(self, args: dict[str, str]) -> int:
        selector = args.get("exercises", "all")
        if selector == "all":
            folder_names = None
        else:
            all_names = self._structure_checker.bank_folder_names()
            folder_names = []
            for token in selector.split(","):
                token = token.strip()
                if token.isdigit():
                    matches = [
                        n for n in all_names if n.startswith(f"ex_{token.zfill(4)}_")
                    ]
                    if not matches:
                        Output.error(
                            f"No exercise with id '{token}' in the bank.", False
                        )
                        return 1
                    folder_names.extend(matches)
                elif token in all_names:
                    folder_names.append(token)
                else:
                    Output.error(f"Exercise '{token}' not found in the bank.", False)
                    return 1

        issues = self._structure_checker.check(folder_names)
        if not issues:
            Output.success("Bank structure is valid.")
            return 0

        Output.error(f"{len(issues)} structure issue(s) found:", show_log_link=False)
        for issue in issues:
            Output.hint(f"  [{issue.exercise}] {issue.message}")
        return 1

    def _publish(self, args: dict[str, str]) -> int:
        target = Path(args["target"])

        bank = Path(BANK_EXERCISES_PATH)
        all_fullnames = sorted(
            d.name for d in bank.iterdir() if d.is_dir() and d.name.startswith("ex_")
        )

        selector = args.get("exercises", "all")
        if selector == "all":
            fullnames = all_fullnames
        else:
            fullnames = []
            for token in selector.split(","):
                token = token.strip()
                if token.isdigit():
                    matches = [
                        f for f in all_fullnames if f.startswith(f"ex_{token.zfill(4)}_")
                    ]
                    if not matches:
                        Output.error(f"No exercise with id '{token}' in the bank.")
                        return 1
                    fullnames.extend(matches)
                elif token in all_fullnames:
                    fullnames.append(token)
                else:
                    Output.error(f"Exercise '{token}' not found in the bank.")
                    return 1

        if not fullnames:
            Output.error("No exercise to publish.")
            return 1

        try:
            with Spinner("Publishing..."):
                published = self._publisher.publish(target, fullnames)
        except PublishError as e:
            Output.error(str(e), False)
            return 1

        Output.success(f"Published {len(published)} exercise(s) to {target}.")
        Output.hint(
            "No git operation was performed: review the diff in the target, then commit and push."
        )

        local_state = [
            rel
            for rel in ("Exercises", ".argos/argos.log", ".argos/sync_base")
            if (target / rel).exists()
        ]
        if local_state:
            Output.warn(
                "The target clone also contains local working state, NOT published: "
                + ", ".join(local_state)
            )
            Output.hint(
                "  Never 'git add .' in the target: stage the published paths explicitly."
            )
        return 0

    def _handle_solution(self, args: dict[str, str]) -> int:
        match args.get("solution_action"):
            case "strip":
                return self._strip_solution(args)
            case "detect":
                return self._detect_solutions(args)
            case other:
                Output.error(f"Unknown solution action '{other}'.")
                return 1

    def _handle_create(self, args: dict[str, str]) -> int:
        create_action = args.get("create_action")
        match create_action:
            case "learning-path":
                return self._create_learning_path(args)
            case "exercise":
                return self._create_exercise()
            case "class":
                return self._create_class(args)
            case _:
                Output.error(f"Unknown create action '{create_action}'.")
                return 1

    def _create_class(self, args: dict[str, str]) -> int:
        ssh = args.get("ssh", False)
        skip_check = args.get("skip_repository_check", False)
        class_name = args["name"]
        lp_id = args["learning_path"]
        csv_path = args.get("from_csv")

        if self._class_manager.get_class(class_name) is not None:
            Output.error(
                f"Class {class_name} already exists.",
                show_log_link=False,
            )
            return 1
        if csv_path:
            try:
                with Spinner("Creating class"):
                    output_path, invalid_students = (
                        self._class_manager.create_class_from_csv(
                            class_name,
                            lp_id,
                            csv_path,
                            skip_check is False,
                            ssh is not False,
                        )
                    )
            except (ValueError, FileNotFoundError) as e:
                Output.error(str(e), show_log_link=False)
                return 1
        else:
            students: list[Student] = []
            print(f"Creating class '{class_name}' (enter an empty name to finish)...")
            while True:
                name = input("Student name: ").strip()
                if not name:
                    break
                repo_url = ""
                first = True
                while first or not REPO_URL_REGEX_FORMAT.match(repo_url):
                    repo_url = input("Repo URL (owner/repo): ").strip()
                    first = False
                    if not REPO_URL_REGEX_FORMAT.match(repo_url):
                        Output.error(
                            "Wrong repo format you must specify: owner/repo",
                            show_log_link=False,
                        )
                if not repo_url:
                    break

                students.append(Student(name=name, repo_url=repo_url))

            if not students:
                Output.error("No students entered. Class not created.")
                return 1
            with Spinner("Creating class"):
                output_path, invalid_students = self._class_manager.create_class(
                    class_name, lp_id, students, skip_check is False, ssh is not False
                )

        if len(invalid_students) > 0:
            Output.warn(
                f"The repositories of the following students couldn't be reached: {', '.join([f"'{s.name}'" for s in invalid_students])}"
            )

        Output.success(f"Sucessfully created class: '{class_name}'")
        Output.path("File", output_path)

        return 0

    def _create_learning_path(self, args: dict[str, str]) -> int:
        lp_id = args["id"]
        based_on = args.get("based_on")

        if based_on:
            try:
                path = self._learning_paths_manager.create_from(lp_id, based_on)
            except (FileNotFoundError, FileExistsError) as e:
                Output.error(str(e))
                return 1
            Output.success("\nLearning path created!")
            Output.path("File", path)
            Output.hint(f"  Based on: {based_on}")
            Output.hint("  Open the file to further customize it.")
            return 0

        print(f"Creating new learning path '{lp_id}'...")

        name = input("Display name: ").strip()
        if not name:
            Output.error("Name cannot be empty.")
            return 1

        raw_count = input("Number of series [1]: ").strip() or "1"
        try:
            count = int(raw_count)
            if count < 1:
                raise ValueError
        except ValueError:
            Output.error("Number of series must be a positive integer.")
            return 1

        series: list[tuple[str, int]] = []
        for i in range(1, count + 1):
            serie_name = input(f"Series {i} name: ").strip()
            if not serie_name:
                Output.error("Series name cannot be empty.")
                return 1
            raw_pts = input(f"Points to complete '{serie_name}': ").strip()
            try:
                pts = int(raw_pts)
                if pts < 1:
                    raise ValueError
            except ValueError:
                Output.error("Points must be a positive integer.", False)
                return 1
            series.append((serie_name, pts))

        try:
            path = self._learning_paths_manager.create(lp_id, name, series)
        except FileExistsError as e:
            Output.error(str(e))
            return 1

        Output.success("\nLearning path created!")
        Output.path("File", path)
        Output.hint("  Open the file to add exercises and further customize it.")
        return 0

    def _create_exercise(self) -> int:
        slug = input("Slug (CamelCase, e.g. PrintHelloWorld): ").strip()
        if not SLUG_REGEX_FORMAT.match(slug):
            Output.error(
                "Slug must be CamelCase (letters and digits, starting with an uppercase letter).",
                show_log_link=False,
            )
            return 1

        lang_raw = (input("Language [c/cpp] (default: c): ").strip().lower() or "c")
        if lang_raw not in ("c", "cpp"):
            Output.error("Language must be 'c' or 'cpp'.", show_log_link=False)
            return 1
        language = ExerciseLanguage(lang_raw)

        try:
            exercise_dir, unit_test_dir = self._exercise_bank_manager.create(slug, language)
        except FileExistsError as e:
            Output.error(str(e))
            return 1

        Output.success("Exercise created!")
        Output.path("Exercise", exercise_dir)
        Output.path("Unit test", unit_test_dir)
        Output.hint("  Open the files to implement the exercise and its test.")

        issues = self._structure_checker.check([exercise_dir.name])
        if issues:
            Output.hint("  Left to fill before the exercise passes check-structure:")
            for issue in issues:
                Output.hint(f"    {issue.message}")
        return 0

    def _strip_solution(self, args: dict[str, str]) -> int:
        exercises = args["exercises"]
        full_scope = self._context.full_scope()
        if exercises == "all":
            raw_exercises = [e.fullname for e in full_scope.exercises]
        else:
            raw_exercises = [e.strip().zfill(4) for e in exercises.split(",")]

        exercise_fullnames: set[str] = set()
        for exercise in raw_exercises:
            if exercise.isdigit():
                exercise_fullname = next(
                    (e.fullname for e in full_scope.exercises if e.id == exercise), None
                )
                if exercise_fullname is None:
                    Output.error(f"Exercise '{exercise}' not found.", False)
                    return 1
                exercise_fullnames.add(exercise_fullname)
            elif exercise not in [e.fullname for e in full_scope.exercises]:
                Output.error(f"Exercise '{exercise}' not found.", False)
                return 1
            else:
                exercise_fullnames.add(exercise)

        self._solution_stripper.strip_solutions(list(exercise_fullnames))
        return 0

    def _detect_solutions(self, args: dict[str, str]) -> int:
        exercises = args.get("exercises", "all")
        full_scope = self._context.full_scope()
        if exercises == "all":
            exercise_fullnames = [e.fullname for e in full_scope.exercises]
        else:
            exercise_fullnames = [e.strip() for e in exercises.split(",")]

        for exercise_fullname in exercise_fullnames:
            if exercise_fullname not in [e.fullname for e in full_scope.exercises]:
                Output.error(f"Exercise '{exercise_fullname}' not found.", False)
                return 1

        found = self._solution_stripper.detect_solutions(exercise_fullnames)
        if not found:
            Output.success("No solution blocks found.")
            return 0

        Output.error(
            f"{len(found)} file(s) contain solution blocks:", show_log_link=False
        )
        for path in found:
            Output.hint(f"  {path}")
        return 1

    def _evaluate(self, args: dict[str, str]) -> int:
        ssh = args.get("ssh", False)
        class_name = args["class_name"]

        class_config = self._class_manager.get_class(class_name)
        if class_config is None:
            Output.error("This class doesn't exist", show_log_link=False)
            return 1

        lp_id = class_config.learning_path_id
        lp = next((lp for lp in self._context.learning_paths if lp.id == lp_id), None)
        if lp is None:
            Output.error(f"Learning path '{lp_id}' not found.", False)
            return 1

        students = list(class_config.students)
        n = len(students)
        scope = self._context.scope_for_learning_path(lp_id)

        with Spinner(f"Cloning {n} repo{'s' if n != 1 else ''}..."):
            valid_students, invalid_students = self._evaluation.synchronize_repos(
                students, lp, ssh is not False
            )

        with Spinner(
            f"Running pipelines {f'({len(valid_students)} valid)' if len(invalid_students) > 0 else ''}..."
        ):
            reports = self._evaluation.run_pipelines(valid_students, scope)

        with Spinner("Computing scores and writing CSV..."):
            scores = self._evaluation.compute_and_write(
                lp, reports, invalid_students, args["output"], scope, valid_students
            )

        self._admin_dashboard_generator.generate(
            lp, scores, invalid_students, Path(ADMIN_DASHBOARD_DATA_FILE_PATH)
        )

        Output.success("Evaluation complete.")
        Output.path("Results", args["output"])
        Output.path("Professor Dashboard", Path(ADMIN_DASHBOARD_INDEX_FILE_PATH))
        return 0

    def _search_exercises(self, args: dict[str, str]) -> int:
        language = ExerciseLanguage(args["language"])
        difficulty = (
            ExerciseDifficulty(args["difficulty"]) if args.get("difficulty") else None
        )
        raw_skills = args.get("skills")
        if raw_skills is None:
            skills = []
        elif isinstance(raw_skills, list):
            skills = raw_skills
        else:
            skills = [raw_skills]
        match_all = not args.get("match_any", False)

        results = self._exercise_search.get_exercises(
            language, difficulty, skills, match_all
        )

        if not results:
            Output.hint("No exercises found matching the given criteria.")
            return 0

        Output.success(f"{len(results)} exercise(s) found:")
        headers = ["Exercise", "Difficulty", "Description", "Skills"]
        rows = [
            [
                exercise.fullname,
                exercise.metadata.difficulty.value,
                exercise.metadata.description,
                ", ".join(exercise.metadata.skills) if exercise.metadata.skills else "—",
            ]
            for exercise in results
        ]
        Output.table(headers, rows, wrap_cols=[2, 3])
        return 0
