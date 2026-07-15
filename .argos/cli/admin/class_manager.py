import json
from pathlib import Path

from config import LearningPathsManager
from config.models import ClassConfig, Student
from git_bindings import GitBindings
from utils.constants import CLASSES_FOLDER_PATH


class ClassManager:
    """
    Creates and loads the classes defined in the .argos/classes folder
    """

    def __init__(
        self, git_bindings: GitBindings, learning_path_manager: LearningPathsManager
    ):
        self._git = git_bindings
        self._learning_path_manager = learning_path_manager

    def get_class(self, name: str) -> ClassConfig | None:
        """
        Get a class config from it's name.
        Returns: ClassConfig on success None if not found.
        Throws an exception if it fails to parse the class file.
        """
        full_path = self._get_full_path(name)
        if not full_path.exists():
            return None

        return ClassConfig.from_json(full_path)

    def create_class_from_csv(
        self,
        name: str,
        learning_path_id: str,
        csv_path: str,
        check_invalid_repos: bool = True,
        use_ssh: bool = False,
    ) -> tuple[Path, list[Student]]:
        """
        Create a class config from a csv file and check if repos exists.

        Returns tuple[output_path, invalidStudents]: the output path and the list of students whose repository is not reachable.
        When check_invalid_repos is False then the invalidStudents list will be empty
        """

        full_path = self._get_full_path(name)
        csv = Path(csv_path)
        if not csv.exists():
            raise FileNotFoundError(f"Unable to find csv path at '{csv_path}'")

        if self._learning_path_manager.get_learning_path(learning_path_id) is None:
            raise ValueError(f"No learningPath exists with id: '{learning_path_id}'")

        config = ClassConfig.from_csv(csv, name, learning_path_id)

        self._create_internal(config, full_path)
        if check_invalid_repos:
            invalid_repos = self._check_invalid_repos(list(config.students), use_ssh)
        else:
            invalid_repos = []

        return full_path, invalid_repos

    def create_class(
        self,
        name: str,
        learning_path_id: str,
        students: list[Student],
        check_invalid_repos: bool = True,
        use_ssh: bool = False,
    ) -> tuple[Path, list[Student]]:
        """
        Creates a class config and check if students repos exists.

        Returns tuple[output_path, invalidStudents]: the output path and the list of students whose repository is not reachable
        When check_invalid_repos is False then the invalidStudents list will be empty
        """

        full_path = self._get_full_path(name)
        config = ClassConfig(name, learning_path_id, tuple(students))

        self._create_internal(config, full_path)
        if check_invalid_repos:
            invalid_repos = self._check_invalid_repos(students, use_ssh)
        else:
            invalid_repos = []

        return full_path, invalid_repos

    def _create_internal(self, config: ClassConfig, path: Path) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            json.dump(config.to_dict(), f, indent=4, ensure_ascii=False)
            f.write("\n")

    def _check_invalid_repos(
        self, students: list[Student], use_ssh: bool
    ) -> list[Student]:
        return list(
            filter(
                lambda s: not self._git.check_repository_exists(s.clone_url(use_ssh)),
                students,
            )
        )

    def _get_full_path(self, name: str) -> Path:
        return Path(CLASSES_FOLDER_PATH) / f"{name}.json"
