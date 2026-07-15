from logging import getLogger
from pathlib import Path

from config import LearningPathsManager
from config.models import LearningPath, Student
from git_bindings import GitBindings
from utils.constants import STUDENT_REPOS_FOLDER_PATH

logger = getLogger(__name__)


class RepositorySynchronizer:
    """
    Clones or pulls repositories for students, then checks validity against the
    expected learning path and returns valid/invalid student lists.
    """

    def __init__(
        self, git_bindings: GitBindings, learning_paths_manager: LearningPathsManager
    ) -> None:
        self._git = git_bindings
        self._learning_paths_manager = learning_paths_manager

    def synchronize(
        self,
        students: list[Student],
        learning_path: LearningPath,
        use_ssh: bool = False,
    ) -> tuple[list[Student], list[Student]]:
        """
        Synchronizes repositories of the given students into the `students` folder.
            - `students`: the students whose repos to clone/pull
            - `learning_path`: the learning path to validate against
            - `use_ssh`: whether to use SSH URLs (default: False)
        Returns: tuple[valid_students, invalid_students]
        """
        Path(STUDENT_REPOS_FOLDER_PATH).mkdir(parents=True, exist_ok=True)
        update_sucess: list[bool] = []
        for s in students:
            update_sucess.append(self._update_repo(s, use_ssh))

        valid_students = [
            s
            for i, s in enumerate(students)
            if update_sucess[i]
            and self._is_valid_repo(
                str(Path(STUDENT_REPOS_FOLDER_PATH) / s.owner), learning_path
            )
        ]
        invalid_students = [s for s in students if s not in valid_students]

        return valid_students, invalid_students

    def _update_repo(self, student: Student, use_ssh: bool) -> bool:
        url = student.clone_url(use_ssh)
        dest = Path(STUDENT_REPOS_FOLDER_PATH) / student.owner

        if (dest / ".git").exists():
            logger.debug(
                "Pulling existing repository for '%s' from '%s' to '%s'.",
                student.name,
                url,
                dest,
            )
            try:
                self._git.pull(str(dest))
                return True
            except Exception as e:
                logger.error(
                    "Failed to pull repository for '%s' from '%s' to '%s': %s",
                    student.name,
                    url,
                    dest,
                    e,
                )
                return False

        logger.debug(
            "Cloning repository for '%s' from '%s' to '%s'.",
            student.name,
            url,
            dest,
        )
        try:
            self._git.clone(url, str(dest))
            return True
        except Exception as e:
            logger.error(
                "Failed cloning repository for '%s' from '%s' to '%s': %s",
                student.name,
                url,
                dest,
                e,
            )
            return False

    def _is_valid_repo(self, repo_path: str, learning_path: LearningPath) -> bool:
        student_learning_path = self._learning_paths_manager.get_learning_path(
            learning_path.id, repo_path
        )

        if student_learning_path is None:
            logger.warning(
                "Learning path with id '%s' not found in the student repo at '%s'.",
                learning_path.id,
                repo_path,
            )
            return False

        if student_learning_path != learning_path:
            logger.warning(
                "Student learning path '%s' does not match the local learning path '%s' for repo at '%s'.",
                student_learning_path.id,
                learning_path.id,
                repo_path,
            )
            return False

        return True
