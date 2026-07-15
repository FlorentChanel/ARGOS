from dataclasses import dataclass
from typing import Any, cast

from .exercise import Exercise


@dataclass(frozen=True)
class Serie:
    """Represents an exercise series within a learning path."""

    name: str
    points_to_complete: int
    exercises: list[Exercise]

    @staticmethod
    def from_json(json: dict[str, Any]) -> "Serie":
        if "name" not in json:
            raise ValueError("Serie JSON is missing 'name' key")
        if "pointsToComplete" not in json:
            raise ValueError("Serie JSON is missing 'pointsToComplete' key")
        if "exercises" not in json:
            raise ValueError("Serie JSON is missing 'exercises' key")

        name = json["name"]
        points_to_complete = json["pointsToComplete"]
        exercises_json = json["exercises"]

        if not isinstance(name, str):
            raise ValueError(f"Serie 'name' should be a string, but found: '{name}'")
        if not isinstance(points_to_complete, int):
            raise ValueError(
                f"Serie 'pointsToComplete' should be an integer, but found: '{points_to_complete}'"
            )
        if not isinstance(exercises_json, list):
            raise ValueError(
                f"Serie 'exercises' should be a list, but found: '{exercises_json}'"
            )

        exercises_json = cast(list[Any], exercises_json)
        if not all(isinstance(item, str) for item in exercises_json):
            raise ValueError(
                f"Serie 'exercises' should be a list of strings, but found non-string in: '{exercises_json}'"
            )

        exercises = [Exercise(ex_id) for ex_id in exercises_json]

        return Serie(
            name=name,
            points_to_complete=points_to_complete,
            exercises=exercises,
        )
