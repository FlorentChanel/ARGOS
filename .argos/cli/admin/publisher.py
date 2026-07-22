import json
import shutil
from logging import getLogger
from pathlib import Path

from admin.solution_stripper import SolutionStripper
from config.models import Exercise
from utils.constants import (
    ARGOS_FOLDER,
    BANK_EXERCISES_PATH,
    CLI_FOLDER,
    DASHBOARDS_FOLDER_PATH,
    DIFFICULTY_LABELS_FILE_NAME,
    HOOKS_FOLDER_PATH,
    LEARNING_PATHS_FOLDER_PATH,
    ROOT_FOLDER,
    SKILLS_LABELS_FILE_NAME,
    TEXT_EXTENSIONS,
    UNIT_TESTS_FOLDER_PATH,
)

logger = getLogger(__name__)

CATALOGUE_BEGIN = "<!-- CATALOGUE:BEGIN -->"
CATALOGUE_END = "<!-- CATALOGUE:END -->"
BANNER_COMMENT = (
    "<!-- Generated at publication from metadata.json — do not edit by hand -->"
)
DIFFICULTY_BADGES = {"easy": "🟢", "medium": "🟡", "hard": "🔴"}
# Display names of the language enum — identical in French and English.
LANGUAGE_LABELS = {"c": "C", "cpp": "C++"}

README_SCAFFOLD = f"""# ARGOS

## Exercises

{CATALOGUE_BEGIN}
{CATALOGUE_END}
"""


class PublishError(Exception):
    pass


class Publisher:
    """Materializes the student repository content from the exercise bank.

    Three generated outputs in one pass: stripped sources, README banners and
    the exercise catalogue. Never runs any git operation — the target is left
    as a working tree to review, commit and push manually.
    """

    def __init__(self, solution_stripper: SolutionStripper) -> None:
        self._stripper = solution_stripper
        self._skills_labels: dict[str, dict[str, str]] = {}
        self._difficulty_labels: dict[str, dict[str, str]] = {}

    def publish(self, target: Path, exercise_fullnames: list[str]) -> list[str]:
        """Publishes the given exercises into the target directory.

        Returns the list of published exercise fullnames (sorted by id).
        Raises PublishError on unbalanced solution markers or missing inputs.
        """
        self._load_labels()

        exercises = [Exercise(fullname) for fullname in sorted(exercise_fullnames)]
        for exercise in exercises:
            if not exercise.bank_exercise_path.exists():
                raise PublishError(
                    f"Exercise '{exercise.fullname}' not found in the bank."
                )

        target.mkdir(parents=True, exist_ok=True)

        for exercise in exercises:
            self._publish_exercise(target, exercise)

        self._copy_shared(target)
        self._write_catalogue(target, exercises)

        return [e.fullname for e in exercises]

    def _load_labels(self) -> None:
        self._skills_labels = self._load_label_table(SKILLS_LABELS_FILE_NAME)
        self._difficulty_labels = self._load_label_table(DIFFICULTY_LABELS_FILE_NAME)

    def _load_label_table(self, filename: str) -> dict[str, dict[str, str]]:
        path = Path(BANK_EXERCISES_PATH) / filename
        if not path.exists():
            raise PublishError(f"Label table not found: {path}")
        return json.loads(path.read_text(encoding="utf-8"))

    def _skill_label(self, key: str, lang: str) -> str:
        return self._skills_labels.get(key, {}).get(lang, key)

    def _difficulty_label(self, key: str, lang: str) -> str:
        return self._difficulty_labels.get(key, {}).get(lang, key)

    def _publish_exercise(self, target: Path, exercise: Exercise) -> None:
        dest = target / ".argos" / "exercises" / exercise.fullname
        if dest.exists():
            shutil.rmtree(dest)
        dest.mkdir(parents=True)

        for src in sorted(exercise.bank_exercise_path.iterdir()):
            if src.is_dir():
                continue
            self._publish_file(src, dest / src.name, exercise)

        test_src = Path(UNIT_TESTS_FOLDER_PATH) / exercise.fullname
        if not test_src.exists():
            raise PublishError(
                f"Unit tests for '{exercise.fullname}' not found at {test_src}."
            )
        test_dest = target / ".argos" / "unitTests" / exercise.fullname
        if test_dest.exists():
            shutil.rmtree(test_dest)
        test_dest.mkdir(parents=True)
        for src in sorted(test_src.iterdir()):
            if src.is_dir():
                continue
            self._publish_file(src, test_dest / src.name, exercise)

        logger.info("Published exercise %s", exercise.fullname)

    def _publish_file(self, src: Path, dest: Path, exercise: Exercise) -> None:
        if src.suffix not in TEXT_EXTENSIONS:
            shutil.copy2(src, dest)
            return

        content = src.read_text(encoding="utf-8")

        begins, ends = self._stripper.count_markers(content)
        if begins != ends:
            raise PublishError(
                f"Unbalanced SOLUTION markers in {src} ({begins} BEGIN / {ends} END). "
                "Fix the markers before publishing."
            )

        content = self._stripper.strip_string(content)

        if src.name in ("README.en.md", "README.fr.md"):
            lang = "en" if src.name == "README.en.md" else "fr"
            content = self._banner(exercise, lang) + content

        dest.write_text(content, encoding="utf-8", newline="")

    def _banner(self, exercise: Exercise, lang: str) -> str:
        meta = exercise.metadata
        badge = DIFFICULTY_BADGES.get(meta.difficulty.value, "")
        difficulty = self._difficulty_label(meta.difficulty.value, lang)
        language = LANGUAGE_LABELS.get(meta.language.value, meta.language.value)
        skills = [self._skill_label(key, lang) for key in meta.skills]

        if lang == "fr":
            language_line = f"**Langage :** {language}"
            difficulty_line = f"**Difficulté :** {badge} {difficulty}"
            skills_header = "**Compétences testées :**"
        else:
            language_line = f"**Language:** {language}"
            difficulty_line = f"**Difficulty:** {badge} {difficulty}"
            skills_header = "**Tested skills:**"

        lines = [
            BANNER_COMMENT,
            "",
            f"# {exercise.id} — {meta.exercise_name}",
            "",
            language_line,
            "",
            difficulty_line,
            "",
            skills_header,
            *[f"- {skill}" for skill in skills],
            "",
            "",
        ]
        return "\n".join(lines)

    def _copy_shared(self, target: Path) -> None:
        argos_dir = target / ".argos"

        # Shared unit-test infrastructure
        self._copy_tree(
            Path(UNIT_TESTS_FOLDER_PATH) / "Common", argos_dir / "unitTests" / "Common"
        )
        shutil.copy2(
            Path(UNIT_TESTS_FOLDER_PATH) / "CMakeLists.txt",
            argos_dir / "unitTests" / "CMakeLists.txt",
        )

        # Ignore rules for per-clone state (argos.log, sync_base/) travel with the repo
        argos_gitignore = Path(ARGOS_FOLDER) / ".gitignore"
        if argos_gitignore.exists():
            shutil.copy2(argos_gitignore, argos_dir / ".gitignore")

        # Bank-level metadata files (schema + label tables)
        bank_dest = argos_dir / "exercises"
        bank_dest.mkdir(parents=True, exist_ok=True)
        for name in (
            "metadata.schema.json",
            SKILLS_LABELS_FILE_NAME,
            DIFFICULTY_LABELS_FILE_NAME,
        ):
            src = Path(BANK_EXERCISES_PATH) / name
            if src.exists():
                shutil.copy2(src, bank_dest / name)

        self._copy_tree(Path(LEARNING_PATHS_FOLDER_PATH), argos_dir / "learningPaths")
        self._copy_tree(Path(HOOKS_FOLDER_PATH), argos_dir / "hooks")
        self._copy_tree(Path(CLI_FOLDER), argos_dir / "cli")
        # Dashboard static assets; data.js is generated locally by 'argos check'.
        self._copy_tree(
            Path(DASHBOARDS_FOLDER_PATH), argos_dir / "dashboards", extra_ignore="data.js"
        )

        # Root-level files
        root = Path(ROOT_FOLDER)
        for name in (".clangd", ".gitignore", "argos.py", "argos.exe"):
            src = root / name
            if src.exists():
                shutil.copy2(src, target / name)

        # GitHub Actions workflows
        github_dir = root / ".github"
        if github_dir.exists():
            self._copy_tree(github_dir, target / ".github")

        # Default CLI config, only when absent (never clobber a student's selection)
        config = target / ".argos-config.json"
        if not config.exists():
            config.write_text('{\n    "learningPaths": []\n}\n', encoding="utf-8")

    def _copy_tree(self, src: Path, dest: Path, extra_ignore: str | None = None) -> None:
        if not src.exists():
            raise PublishError(f"Expected source folder not found: {src}")
        if dest.exists():
            shutil.rmtree(dest)
        patterns = ["__pycache__", "*.pyc"]
        if extra_ignore is not None:
            patterns.append(extra_ignore)
        shutil.copytree(src, dest, ignore=shutil.ignore_patterns(*patterns))

    def _write_catalogue(self, target: Path, exercises: list[Exercise]) -> None:
        readme = target / "README.md"
        content = (
            readme.read_text(encoding="utf-8") if readme.exists() else README_SCAFFOLD
        )

        if CATALOGUE_BEGIN not in content or CATALOGUE_END not in content:
            logger.warning(
                "Catalogue markers missing in %s — appending them at the end.", readme
            )
            content = content.rstrip() + f"\n\n{CATALOGUE_BEGIN}\n{CATALOGUE_END}\n"

        rows = [
            "| ID | Exercise | Tested skills | Difficulty |",
            "|----|----------|---------------|------------|",
        ]
        for exercise in exercises:
            meta = exercise.metadata
            base = f".argos/exercises/{exercise.fullname}"
            name_cell = (
                f"[{meta.exercise_name}]({base}/README.en.md)"
                f" · [fr]({base}/README.fr.md)"
            )
            skills = ", ".join(self._skill_label(k, "en") for k in meta.skills)
            badge = DIFFICULTY_BADGES.get(meta.difficulty.value, "")
            difficulty = f"{badge} {self._difficulty_label(meta.difficulty.value, 'en')}"
            rows.append(f"| {exercise.id} | {name_cell} | {skills} | {difficulty} |")

        table = "\n".join(rows)
        before = content.split(CATALOGUE_BEGIN)[0]
        after = content.split(CATALOGUE_END)[1]
        content = f"{before}{CATALOGUE_BEGIN}\n{table}\n{CATALOGUE_END}{after}"

        readme.write_text(content, encoding="utf-8", newline="")
        logger.info("Catalogue written with %d exercises", len(exercises))
