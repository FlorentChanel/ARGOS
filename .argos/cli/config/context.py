from logging import getLogger
from pathlib import Path

from utils.constants import ROOT_FOLDER
from utils.exercise_utils import ExerciseUtils

from .argos_config import ArgosConfig
from .learning_paths_manager import LearningPathsManager
from .models import (
    Exercise,
    ExerciseScope,
    LearningPath,
    Serie,
)

logger = getLogger(__name__)


def _resolve_exercise(scope: ExerciseScope, target: str) -> Exercise | None:
    exact = next((e for e in scope.exercises if e.fullname == target), None)
    if exact:
        return exact
    normalized = target.zfill(4)
    return next((e for e in scope.exercises if e.id == normalized), None)


class Context:
    """
    Represents the context of the ARGOS CLI, containing all the necessary information and state for executing commands.
    """

    def __init__(
        self, learning_paths_manager: LearningPathsManager, argos_config: ArgosConfig
    ):
        self._learning_paths_manager = learning_paths_manager
        self._argos_config = argos_config

    @property
    def learning_paths(self) -> list[LearningPath]:
        return self._get_selected_learning_paths()

    def _get_selected_learning_paths(self) -> list[LearningPath]:
        paths: list[LearningPath] = []
        for path_id in self._argos_config.learning_paths:
            path = self._learning_paths_manager.get_learning_path(path_id)
            if path is None:
                logger.warning(
                    "Learning path with id '%s' not found in the learning paths manager.",
                    path_id,
                )
                continue
            paths.append(path)

        return paths

    def full_scope(self) -> ExerciseScope:
        return self._build_exercise_scope()

    def scope_for_exercise(self, target: str) -> ExerciseScope:
        scope = self.full_scope()
        exercise = _resolve_exercise(scope, target)
        if exercise is None:
            raise ValueError(f"Exercise '{target}' is not in the current scope.")
        return ExerciseScope(
            root=scope.root,
            exercises=[exercise],
            series_by_exercise={exercise.id: scope.series_by_exercise[exercise.id]},
        )

    def scope_for_touched_exercises(self) -> ExerciseScope:
        scope = self.full_scope()
        touched = [e for e in scope.exercises if not ExerciseUtils.is_untouched(e)]
        return ExerciseScope(
            root=scope.root,
            exercises=touched,
            series_by_exercise={e.id: scope.series_by_exercise[e.id] for e in touched},
        )

    def scope_for_learning_path(self, path_id: str) -> ExerciseScope:
        path = next((p for p in self.learning_paths if p.id == path_id), None)
        if path is None:
            raise ValueError(
                f"Learning path '{path_id}' is not among the selected paths."
            )
        return self._build_exercise_scope(paths=[path])

    def _build_exercise_scope(
        self, paths: list[LearningPath] | None = None
    ) -> ExerciseScope:
        exercises_by_id: dict[str, Exercise] = {}
        series_by_exercise: dict[str, list[tuple[LearningPath, Serie]]] = {}

        for path in paths if paths is not None else self.learning_paths:
            for serie in path.series:
                for exercise in serie.exercises:
                    if exercise.id not in exercises_by_id:
                        exercises_by_id[exercise.id] = exercise
                    series_by_exercise.setdefault(exercise.id, []).append((path, serie))

        return ExerciseScope(
            root=Path(ROOT_FOLDER),
            exercises=list(exercises_by_id.values()),
            series_by_exercise=series_by_exercise,
        )
