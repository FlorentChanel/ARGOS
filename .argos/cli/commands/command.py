from abc import ABC, abstractmethod
from argparse import ArgumentParser


class Command(ABC):
    help: str

    @abstractmethod
    def configure(self, parser: ArgumentParser) -> None: ...

    @abstractmethod
    def execute(self, args: dict[str, str]) -> int: ...
