from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from config.models import ExerciseScope

from .models import StepResult

PayloadT = TypeVar("PayloadT")


class PipelineStep(ABC, Generic[PayloadT]):
    @abstractmethod
    def run(self, scope: ExerciseScope) -> StepResult[PayloadT]: ...
