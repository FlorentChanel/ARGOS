import shutil
from logging import getLogger
from pathlib import Path

from git_bindings import GitBindings, MergeFileResultKind
from utils.constants import (
    EXERCISE_FOLDER_PATH,
    ROOT_FOLDER,
    SYNC_BASE_PATH,
    SYNC_FILES_TO_IGNORE,
)
from utils.exercise_utils import ExerciseUtils

from .context import Context
from .models import Exercise

logger = getLogger(__name__)


def _prompt_keep(label: str, default_keep: bool = True) -> bool:
    hint = "[Y/n]" if default_keep else "[y/N]"
    answer = input(f"  {label} {hint}: ").strip().lower()
    if not answer:
        return default_keep
    return answer.startswith("y")


class WorkspaceSynchronizer:
    """Synchronizes exercises between the exercise bank and the root workdir.

    New exercises are copied from the bank to the workspace and to a sync base
    (.argos/sync_base/). On subsequent syncs, each source file is merged using
    git merge-file (student <- base <- bank), preserving student work while
    pulling in structural changes from the bank. Conflicts are flagged with
    standard merge conflict markers.
    """

    def __init__(self, context: Context, git: GitBindings) -> None:
        self._context = context
        self._git = git

    def override_all(self) -> None:
        """Override all exercises with the versions from the exercise bank, even if they where modified locally.
        Also overrides the locally stored baseline for the exercises. Use with caution as this will discard all local changes to the exercises."""

        expected = {ex.fullname: ex for ex in self._context.full_scope().exercises}
        workspace_ids = self._get_workspace_exercise_ids()
        orphaned_ids = workspace_ids - set(expected)

        for ex in self._context.full_scope().exercises:
            self._copy_exercise(ex, override=True)

        for ex_id in sorted(orphaned_ids):
            self._remove_orphaned(Exercise(ex_id))

    def synchronize(self) -> None:
        Path(EXERCISE_FOLDER_PATH).mkdir(parents=True, exist_ok=True)
        Path(SYNC_BASE_PATH).mkdir(parents=True, exist_ok=True)

        expected = {ex.fullname: ex for ex in self._context.full_scope().exercises}
        workspace_ids = self._get_workspace_exercise_ids()

        new_ids = set(expected) - workspace_ids
        orphaned_ids = workspace_ids - set(expected)
        existing_ids = set(expected) & workspace_ids

        for ex_id in sorted(new_ids):
            self._copy_exercise(expected[ex_id])

        for ex_id in sorted(orphaned_ids):
            self._remove_orphaned(Exercise(ex_id))

        had_conflicts = False
        for ex_id in sorted(existing_ids):
            if self._sync_exercise_source(expected[ex_id]):
                had_conflicts = True

        if had_conflicts:
            logger.warning(
                "Finished synchronization with conflicts. Please resolve <<<<<<< markers in the affected files before building."
            )

    def has_uncommitted_changes(self) -> bool:
        if not self._git.is_repository_clean(ROOT_FOLDER):
            return True

        return False

    def _get_workspace_exercise_ids(self) -> set[str]:
        root = Path(EXERCISE_FOLDER_PATH)
        if not root.exists():
            return set()
        return {d.name for d in root.iterdir() if d.is_dir()}

    def _copy_exercise(self, exercise: Exercise, override: bool = False) -> None:
        if not exercise.bank_exercise_path.exists():
            logger.warning(
                "Exercise '%s' not found in bank at %s",
                exercise.id,
                exercise.bank_exercise_path,
            )
            return

        shutil.copytree(
            exercise.bank_exercise_path,
            exercise.root_path,
            ignore=shutil.ignore_patterns(*SYNC_FILES_TO_IGNORE),
            dirs_exist_ok=override,
        )

        # We copy a fresh version of the exercise to the sync base
        if exercise.base_path.exists():
            shutil.rmtree(exercise.base_path)

        shutil.copytree(
            exercise.bank_exercise_path,
            exercise.base_path,
            ignore=shutil.ignore_patterns(*SYNC_FILES_TO_IGNORE),
        )
        logger.debug("Copied exercise %s to workspace and sync base", exercise.id)

    def _sync_exercise_source(self, exercise: Exercise) -> bool:
        """
        returns true if there are merge conflicts in at least one source file, false otherwise
        """
        if not exercise.base_path.exists():
            shutil.copytree(
                exercise.bank_exercise_path,
                exercise.base_path,
                ignore=shutil.ignore_patterns(*SYNC_FILES_TO_IGNORE),
            )
            logger.warning(
                "No sync base found for '%s' — initialized from bank. Student files kept as-is.",
                exercise.id,
            )
            return False

        had_conflicts = False

        for bank_file in exercise.bank_exercise_path.iterdir():
            if not ExerciseUtils.is_source_file(bank_file):
                if ExerciseUtils.is_copy_only_file(bank_file):
                    logger.debug("Copying copy_only file %s", bank_file.name)
                    shutil.copy2(bank_file, exercise.root_path / bank_file.name)
                continue

            student_file = exercise.root_path / bank_file.name
            base_file = exercise.base_path / bank_file.name

            if not student_file.exists():
                shutil.copy2(bank_file, student_file)
                shutil.copy2(bank_file, base_file)
                logger.debug("Added new file %s to workspace", bank_file.name)
                continue

            if not base_file.exists():
                shutil.copy2(bank_file, base_file)
                logger.debug("Initialized base for new file %s", bank_file.name)
                continue

            merge_result = self._git.merge_file(
                str(student_file), str(base_file), str(bank_file)
            )

            match merge_result:
                case MergeFileResultKind.SUCCESS:
                    logger.debug("Merged %s/%s cleanly", exercise.id, bank_file.name)
                case MergeFileResultKind.CONFLICTS:
                    had_conflicts = True
                    logger.warning(
                        "Merge conflict in '%s/%s' — resolve <<<<<<< markers before building.",
                        exercise.id,
                        bank_file.name,
                    )
                case MergeFileResultKind.ERROR:
                    logger.error(
                        "Error merging '%s/%s'",
                        exercise.id,
                        bank_file.name,
                    )
                    # We raise an error since a command execution error would likely happen on every file.
                    raise RuntimeError(
                        f"Error merging '{exercise.id}/{bank_file.name}' — see log for details."
                    )

        # Remove any source files that are no longer present in the bank.
        for file in exercise.root_path.iterdir():
            if (
                not ExerciseUtils.is_source_file(file)
                or (exercise.bank_exercise_path / file.name).exists()
            ):
                continue

            if ExerciseUtils.is_untouched(exercise):
                file.unlink()
                logger.debug(
                    "Removed orphaned source file %s/%s (untouched)",
                    exercise.id,
                    file.name,
                )

        # Advance the base to the new bank version for future merges.
        shutil.rmtree(exercise.base_path)
        shutil.copytree(
            exercise.bank_exercise_path,
            exercise.base_path,
            ignore=shutil.ignore_patterns(*SYNC_FILES_TO_IGNORE),
        )

        return had_conflicts

    def _remove_orphaned(self, exercise: Exercise) -> None:
        def _remove() -> None:
            if exercise.root_path.exists():
                shutil.rmtree(exercise.root_path)

            if exercise.base_path.exists():
                shutil.rmtree(exercise.base_path)

        if ExerciseUtils.is_untouched(exercise):
            _remove()
            logger.info("Removed orphaned exercise %s (untouched)", exercise.id)
        else:
            logger.info(
                "\n  Exercise '%s' is no longer in your learning path but has been modified.",
                exercise.id,
            )
            if not _prompt_keep(
                f"Keep '{exercise.id}' in workspace anyway?", default_keep=True
            ):
                _remove()
                logger.info(
                    "Removed orphaned exercise %s (user confirmed)", exercise.id
                )
            else:
                logger.info("Kept orphaned exercise %s (user kept)", exercise.id)
