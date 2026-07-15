from dataclasses import replace
from multiprocessing import Pool, freeze_support
from pathlib import Path

from config.models import ExerciseScope, Student
from pipeline import PipelineReport, ProcessPipeline
from utils.constants import STUDENT_REPOS_FOLDER_PATH


def _run_one(
    args: tuple[ProcessPipeline, ExerciseScope, Student],
) -> tuple[str, PipelineReport]:
    pipeline, scope, student = args
    return student.name, pipeline.run(
        replace(scope, root=Path(STUDENT_REPOS_FOLDER_PATH) / student.owner)
    )


class MultipleProjectRunner:
    def __init__(self, process_pipeline: ProcessPipeline) -> None:
        self._pipeline = process_pipeline

    def run_all(
        self, students: list[Student], scope: ExerciseScope
    ) -> dict[str, PipelineReport]:
        freeze_support()  # This is to avoid issues in the PyInstaller executable when using multiprocessing on Windows (https://pyinstaller.org/en/stable/common-issues-and-pitfalls.html#multi-processing)
        with Pool() as pool:
            results = pool.map(_run_one, [(self._pipeline, scope, s) for s in students])
        return dict(results)
