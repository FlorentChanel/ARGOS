import csv
from dataclasses import replace
from logging import getLogger
from pathlib import Path

from config.models import (
    ExerciseScope,
    LearningPath,
    Student,
)
from pipeline import PipelineReport
from scoring import ScoreCalculator, ScoreSummary
from tests.tamper_checker import TamperChecker
from utils.constants import STUDENT_REPOS_FOLDER_PATH

from .multiple_project_runner import MultipleProjectRunner
from .repository_synchronizer import RepositorySynchronizer

logger = getLogger(__name__)


class Evaluation:
    """Class responsible for evaluating student exercises. it syncrhonizes the repositories, runs the pipelines and computes the scores."""

    def __init__(
        self,
        multiple_project_runner: MultipleProjectRunner,
        score_calculator: ScoreCalculator,
        repository_synchronizer: RepositorySynchronizer,
        tamper_checker: TamperChecker | None = None,
    ) -> None:
        self._runner = multiple_project_runner
        self._scorer = score_calculator
        self._repository_synchronizer = repository_synchronizer
        self._tamper_checker = tamper_checker or TamperChecker()

    def synchronize_repos(
        self,
        students: list[Student],
        learning_path: LearningPath,
        use_ssh: bool = False,
    ) -> tuple[list[Student], list[Student]]:
        """
        Synchronizes student repositories and returns valid and invalid students.

        A valid student is one whose repository was successfully cloned/pulled and has the specified learning path selected and the same as the one in the local config.
        """
        return self._repository_synchronizer.synchronize(
            students, learning_path, use_ssh
        )

    def run_pipelines(
        self,
        valid_students: list[Student],
        scope: ExerciseScope,
    ) -> dict[str, PipelineReport]:
        """
        Runs the pipeline for all valid students and returns a dictionary mapping student names to their respective pipeline reports.
        """
        return self._runner.run_all(valid_students, scope)

    def compute_and_write(
        self,
        learning_path: LearningPath,
        reports: dict[str, PipelineReport],
        invalid_students: list[Student],
        output_csv_path: str,
        scope: ExerciseScope,
        valid_students: list[Student] | None = None,
    ) -> dict[str, ScoreSummary]:
        """
        Computes scores for all students, writes them to a CSV file and return the scores for each student.
        """
        name_to_owner = {s.name: s.owner for s in (valid_students or [])}
        scores = self._score_all(reports, scope, name_to_owner)
        self._write_csv(learning_path, scores, invalid_students, output_csv_path)
        return scores

    def _score_all(
        self,
        reports: dict[str, PipelineReport],
        scope: ExerciseScope,
        name_to_owner: dict[str, str] | None = None,
    ) -> dict[str, ScoreSummary]:
        result: dict[str, ScoreSummary] = {}
        for student_name, report in reports.items():
            tampered_by_exercise: dict[str, bool] = {}
            if name_to_owner and student_name in name_to_owner:
                student_root = (
                    Path(STUDENT_REPOS_FOLDER_PATH) / name_to_owner[student_name]
                )
                tampered_by_exercise = self._tamper_checker.check(
                    student_root, scope.exercises
                )
            result[student_name] = self._scorer.compute(
                report, replace(scope, root=student_name), tampered_by_exercise
            )
        return result

    def _write_csv(
        self,
        lp: LearningPath,
        scores: dict[str, ScoreSummary],
        invalid_students: list[Student],
        output_path: str,
    ) -> None:
        serie_names = [s.name for s in lp.series]
        headers = (
            ["student", "valid_repo"]
            + [h for n in serie_names for h in (f"{n}_score", f"{n}_met")]
            + ["total", "tampered"]
        )

        with open(output_path, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(headers)
            for student_name, summary in scores.items():
                lp_result = next(r for r in summary.learning_paths if r.id == lp.id)
                row: list[str | int | bool] = [student_name, True]
                for serie in lp_result.series:
                    row += [serie.points_earned, serie.completed]
                row.append(sum(s.points_earned for s in lp_result.series))
                any_tampered = any(
                    ex.tampered for serie in lp_result.series for ex in serie.exercises
                )
                row.append(any_tampered)
                writer.writerow(row)

            for student in invalid_students:
                writer.writerow([student.name, False] + (["N/A"] * (len(headers) - 2)))
