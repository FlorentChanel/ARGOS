import json
from logging import getLogger
from pathlib import Path

from utils.constants import ARGOS_FOLDER_NAME, LEARNING_PATHS_FOLDER_NAME, ROOT_FOLDER

from .models import LearningPath

logger = getLogger(__name__)


class LearningPathsManager:
    def __init__(self):
        self._cache: dict[str, list[LearningPath]] = {}

    def get_learning_paths(self, root_path: str = ROOT_FOLDER) -> list[LearningPath]:
        """
        Returns the list of learning paths in the given root folder.
        """
        if root_path not in self._cache:
            self._cache[root_path] = self._load_all(Path(root_path))
        return self._cache[root_path]

    def get_learning_path(
        self, id: str, root_path: str = ROOT_FOLDER
    ) -> LearningPath | None:
        """
        Returns the learning path with the given ID, or None if not found.
        """
        return next(
            (lp for lp in self.get_learning_paths(root_path) if lp.id == id), None
        )

    def create(self, id: str, name: str, series: list[tuple[str, int]]) -> Path:
        """
        Creates a new learning path file with the given ID, name, and series.
        It saves the file to the root learning paths folder.

        Args:
            id: The ID of the new learning path (used as the filename stem).
            name: The display name of the new learning path.
            series: A list of tuples representing the series names and their points to complete.

        Returns:
            The path to the newly created learning path file.
        """
        output_path = self._folder() / f"{id}.json"
        if output_path.exists():
            raise FileExistsError(
                f"Learning path '{id}' already exists at {output_path}"
            )

        data = {
            "$schema": "./learningPath.schema.json",
            "name": name,
            "series": [
                {
                    "name": serie_name,
                    "pointsToComplete": points,
                    "exercises": [],
                }
                for serie_name, points in series
            ],
        }
        output_path.write_text(json.dumps(data, indent=2, ensure_ascii=False))
        self._cache.clear()
        return output_path

    def create_from(self, id: str, based_on_id: str) -> Path:
        """
        Creates a new learning path file from an existing one.
        It saves the file to the root learning paths folder.

        Args:
            id: The ID of the new learning path.
            based_on_id: The ID of the existing learning path to use as a template.

        Returns:
            The path to the newly created learning path file.
        """
        template_path = self._folder() / f"{based_on_id}.json"
        if not template_path.exists():
            raise FileNotFoundError(
                f"Template learning path '{based_on_id}' not found."
            )

        output_path = self._folder() / f"{id}.json"
        if output_path.exists():
            raise FileExistsError(
                f"Learning path '{id}' already exists at {output_path}"
            )

        data = json.loads(template_path.read_text())
        data["id"] = id
        output_path.write_text(json.dumps(data, indent=2, ensure_ascii=False))
        self._cache.clear()
        return output_path

    def _folder(self) -> Path:
        return Path(ROOT_FOLDER) / ARGOS_FOLDER_NAME / LEARNING_PATHS_FOLDER_NAME

    def _load_all(self, root: Path) -> list[LearningPath]:
        folder = root / ARGOS_FOLDER_NAME / LEARNING_PATHS_FOLDER_NAME
        learning_paths: list[LearningPath] = []
        for path in folder.glob("*.json"):
            if path.suffixes == [".schema", ".json"]:
                continue
            try:
                learning_paths.append(LearningPath.from_json(path))
            except ValueError as e:
                logger.warning("Ignoring '%s': %s", path.name, e)
        return learning_paths
