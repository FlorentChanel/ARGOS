from dataclasses import dataclass
from pathlib import Path

from .exercise import Exercise
from .learning_path import LearningPath
from .serie import Serie


@dataclass(frozen=True)
class ExerciseScope:
    """Computed view over the selected learning paths.

    Built once at startup. Optimized for the two access patterns:
    - the pipeline iterating physical exercises to build/test
    - scoring looking up which (path, serie) an exercise contributes to
    """

    root: Path
    exercises: list[Exercise]
    series_by_exercise: dict[str, list[tuple[LearningPath, Serie]]]

    def contains(self, target: str) -> bool:
        if "_" in target:
            return any(e.fullname == target for e in self.exercises)
        return target.zfill(4) in self.series_by_exercise

    def series_for(
        self, exercise_id: str
    ) -> list[tuple[LearningPath, Serie]]:
        return self.series_by_exercise.get(exercise_id, [])
