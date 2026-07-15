from dataclasses import dataclass
from json import loads
from pathlib import Path
from typing import Any, cast

from .serie import Serie


@dataclass(frozen=True)
class LearningPath:
    """Represents a learning path in the ARGOS CLI configuration."""

    file_name: str
    id: str
    name: str
    series: list[Serie]

    @staticmethod
    def from_json(path: Path) -> "LearningPath":
        """Creates a LearningPath instance from a JSON file."""
        with open(path, "r") as f:
            json_data: dict[str, Any] = loads(f.read())

        if "name" not in json_data:
            raise ValueError("LearningPath JSON is missing 'name' key")

        if "series" not in json_data:
            raise ValueError("LearningPath JSON is missing 'series' key")

        name_json = json_data["name"]
        series_json = json_data["series"]

        if not isinstance(name_json, str):
            raise ValueError(
                f"LearningPath 'name' should be a string, but found: '{name_json}'"
            )

        if not isinstance(series_json, list):
            raise ValueError(
                f"LearningPath 'series' should be a list, but found: '{series_json}'"
            )

        series_json = cast(list[Any], series_json)

        if not all(isinstance(item, dict) for item in series_json):
            raise ValueError(
                f"LearningPath 'series' should be a list of objects, but found non-object in: '{series_json}'"
            )

        series = [Serie.from_json(s) for s in series_json]

        return LearningPath(
            file_name=path.name,
            id=path.stem,
            name=name_json,
            series=series,
        )
