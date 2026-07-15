from config.models import Exercise, ExerciseScope
from config.models.learning_path import LearningPath
from config.models.serie import Serie
from pipeline import PipelineReport
from tests.models import TestSuite

from .score_summary import (
    ExerciseResult,
    LearningPathResult,
    ScoreSummary,
    SerieResult,
)


class ScoreCalculator:
    def compute(
        self,
        report: PipelineReport,
        scope: ExerciseScope,
        tampered_by_exercise: dict[str, bool] | None = None,
    ) -> ScoreSummary:
        """
        Computes scores for a given pipeline report and exercise scope.

        Params:
            report: The pipeline report containing test results and other relevant data.
            scope: The exercise scope defining which exercises are relevant for scoring.
            tampered_by_exercise: Optional dictionary indicating if an exercise was tampered with.

        Returns:
            A ScoreSummary object containing the computed scores for the learning paths, series, and exercises.
        """
        results_by_exercise = self._extract_test_results(report)
        compilation_output_by_exercise = self._extract_compilation_output(report)
        gtest_output_by_exercise = self._extract_gtest_output(report)
        tampered = tampered_by_exercise or {}

        seen_lp_ids: set[str] = set()
        learning_paths: list[LearningPath] = []
        for series_list in scope.series_by_exercise.values():
            for lp, _ in series_list:
                if lp.id not in seen_lp_ids:
                    seen_lp_ids.add(lp.id)
                    learning_paths.append(lp)

        return ScoreSummary(
            learning_paths=[
                self._build_learning_path_result(
                    lp,
                    scope,
                    results_by_exercise,
                    compilation_output_by_exercise,
                    gtest_output_by_exercise,
                    tampered,
                )
                for lp in learning_paths
            ]
        )

    def _build_learning_path_result(
        self,
        lp: LearningPath,
        scope: ExerciseScope,
        results_by_exercise: dict[str, TestSuite],
        compilation_output_by_exercise: dict[str, str | None],
        gtest_output_by_exercise: dict[str, str | None],
        tampered_by_exercise: dict[str, bool],
    ) -> LearningPathResult:
        return LearningPathResult(
            id=lp.id,
            name=lp.name,
            series=[
                self._build_serie_result(
                    serie,
                    scope,
                    results_by_exercise,
                    compilation_output_by_exercise,
                    gtest_output_by_exercise,
                    tampered_by_exercise,
                )
                for serie in lp.series
            ],
        )

    def _build_serie_result(
        self,
        serie: Serie,
        scope: ExerciseScope,
        results_by_exercise: dict[str, TestSuite],
        compilation_output_by_exercise: dict[str, str | None],
        gtest_output_by_exercise: dict[str, str | None],
        tampered_by_exercise: dict[str, bool],
    ) -> SerieResult:
        exercises = [
            self._build_exercise_result(
                exercise,
                results_by_exercise.get(exercise.id),
                compilation_output_by_exercise.get(exercise.id),
                gtest_output_by_exercise.get(exercise.id),
                tampered_by_exercise.get(exercise.id, False),
            )
            for exercise in serie.exercises
            if scope.contains(exercise.id)
        ]
        return SerieResult(
            name=serie.name,
            points_earned=sum(e.points_earned for e in exercises),
            points_to_complete=serie.points_to_complete,
            exercises=exercises,
        )

    def _extract_test_results(self, report: PipelineReport) -> dict[str, TestSuite]:
        results: dict[str, TestSuite] = {}
        for ex_id, steps in report.exercise_results.items():
            unit_tests = steps.unit_tests
            if unit_tests.skipped or unit_tests.data.suite is None:
                continue
            results[ex_id] = unit_tests.data.suite
        return results

    def _extract_compilation_output(
        self, report: PipelineReport
    ) -> dict[str, str | None]:
        result: dict[str, str | None] = {}
        for ex_id, steps in report.exercise_results.items():
            ninja_result = steps.ninja
            if ninja_result.skipped:
                result[ex_id] = None
            else:
                result[ex_id] = ninja_result.data.compilation_output
        return result

    def _extract_gtest_output(self, report: PipelineReport) -> dict[str, str | None]:
        result: dict[str, str | None] = {}
        for ex_id, steps in report.exercise_results.items():
            unit_tests = steps.unit_tests
            if unit_tests.skipped or unit_tests.data.suite is None:
                result[ex_id] = None
            else:
                result[ex_id] = unit_tests.data.suite.output
        return result

    def _build_exercise_result(
        self,
        exercise: Exercise,
        suite: TestSuite | None,
        compilation_output: str | None = None,
        gtest_output: str | None = None,
        tampered: bool = False,
    ) -> ExerciseResult:
        if suite is None:
            return ExerciseResult(
                exercise_id=exercise.id,
                exercise_name=exercise.metadata.exercise_name,
                skills=exercise.metadata.skills,
                points_earned=0,
                points_available=exercise.points,
                total_tests=None,
                failed_tests=None,
                compilation_output=compilation_output,
                test_results=None,
                gtest_output=gtest_output,
                tampered=tampered,
            )
        passed = suite.failed_tests == 0
        test_results: list[dict[str, object]] = [
            {"name": case.name, "success": case.success, "message": case.message}
            for case in suite.test_cases
        ]
        return ExerciseResult(
            exercise_id=exercise.id,
            exercise_name=exercise.metadata.exercise_name,
            skills=exercise.metadata.skills,
            points_earned=exercise.points if passed else 0,
            points_available=exercise.points,
            total_tests=suite.total_tests,
            failed_tests=suite.failed_tests,
            compilation_output=compilation_output,
            test_results=test_results,
            gtest_output=gtest_output,
            tampered=tampered,
        )
