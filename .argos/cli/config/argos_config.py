from json import dumps, loads
from pathlib import Path

from utils.constants import ROOT_CONFIG_PATH


class ArgosConfig:
    def __init__(self):
        self._config_path = Path(ROOT_CONFIG_PATH)
        self.learning_paths = self._parse_config()

    def save_config(self) -> None:
        """
        Saves the current learningPaths to the config file. If the file does not exist, it creates it.
        """
        config_data = {"learningPaths": self.learning_paths}
        with open(self._config_path, "w") as f:
            f.write(dumps(config_data, indent=4))

    def add_learning_path(self, learning_path: str) -> None:
        """
        Adds a learning path to the config and saves it. If the learning path already exists, it does not add it again.
        """
        if learning_path not in self.learning_paths:
            self.learning_paths.append(learning_path)
            self.save_config()

    def remove_learning_path(self, learning_path: str) -> None:
        """
        Removes a learning path from the config and saves it. If the learning path does not exist, it does nothing.
        """
        if learning_path in self.learning_paths:
            self.learning_paths.remove(learning_path)
            self.save_config()

    def _parse_config(self) -> list[str]:
        """
        Parses the root .argos-config file and returns the list of selected learningPaths.
        Creates a default config (empty selection) if the file does not exist:
        the file is per-user state, untracked, so fresh clones start without it.

        It does not validate if the learningPaths exist or if they are valid. but checks if the learningPaths are strings and if the learningPaths key is present in the config file.
        """
        if not self._config_path.exists():
            self._config_path.write_text(
                dumps({"learningPaths": []}, indent=4), encoding="utf-8"
            )
            return []

        with open(self._config_path, "r") as f:
            config_data = loads(f.read())

        if "learningPaths" not in config_data:
            raise ValueError("Config file is missing 'learningPaths' key")

        if not isinstance(config_data["learningPaths"], list):
            raise ValueError("'learningPaths' should be a list")

        for path in config_data["learningPaths"]:
            if not isinstance(path, str):
                raise ValueError(
                    f"All learningPaths should be strings, but found a non-string value: '{path}'"
                )

        return config_data["learningPaths"]
