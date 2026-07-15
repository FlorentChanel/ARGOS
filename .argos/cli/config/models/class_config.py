import csv
from dataclasses import dataclass
from json import loads
from pathlib import Path
from typing import Any


@dataclass(frozen=True)
class Student:
    name: str
    repo_url: str

    @property
    def owner(self) -> str:
        return self.repo_url.split("/")[0]

    def clone_url(self, ssh: bool = False) -> str:
        if ssh:
            return f"git@github.com:{self.repo_url}.git"
        return f"https://github.com/{self.repo_url}.git"

    @staticmethod
    def _from_dict(data: dict[str, Any]) -> "Student":
        if "name" not in data:
            raise ValueError("Student entry is missing 'name' key")
        if "repoUrl" not in data:
            raise ValueError("Student entry is missing 'repoUrl' key")
        return Student(name=str(data["name"]), repo_url=str(data["repoUrl"]))


@dataclass(frozen=True)
class ClassConfig:
    name: str
    learning_path_id: str
    students: tuple[Student, ...]

    @staticmethod
    def from_json(path: Path) -> "ClassConfig":
        with open(path, "r", encoding="utf-8") as f:
            data: dict[str, Any] = loads(f.read())

        if "learningPath" not in data:
            raise ValueError("Class JSON is missing 'learningPath' key")
        if "students" not in data:
            raise ValueError("Class JSON is missing 'students' key")

        lp_id = data["learningPath"]
        if not isinstance(lp_id, str):
            raise ValueError(f"'learningPath' must be a string, got: {lp_id!r}")

        students_data = data["students"]
        if not isinstance(students_data, list):
            raise ValueError(f"'students' must be a list, got: {students_data!r}")

        return ClassConfig(
            name=path.stem,
            learning_path_id=lp_id,
            students=tuple(Student._from_dict(s) for s in students_data),
        )

    @staticmethod
    def from_csv(csv_path: Path, class_name: str, learning_path_id: str) -> "ClassConfig":
        students: list[Student] = []
        with open(csv_path, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            if reader.fieldnames is None or "name" not in reader.fieldnames or "repoUrl" not in reader.fieldnames:
                raise ValueError("CSV must have 'name' and 'repoUrl' columns")
            for row in reader:
                name = row["name"].strip()
                repo_url = row["repoUrl"].strip()
                if not name or not repo_url:
                    continue
                students.append(Student(name=name, repo_url=repo_url))

        return ClassConfig(
            name=class_name,
            learning_path_id=learning_path_id,
            students=tuple(students),
        )

    def to_dict(self) -> dict[str, Any]:
        return {
            "learningPath": self.learning_path_id,
            "students": [{"name": s.name, "repoUrl": s.repo_url} for s in self.students],
        }
