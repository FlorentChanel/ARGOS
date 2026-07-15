import sys
from logging import DEBUG
from os import path
from pathlib import Path

LOG_LEVEL = DEBUG

CLI_NAME = "argos"
CLI_VERSION = "0.2.0"
CLI_VERSION_STRING = f"{CLI_NAME} version {CLI_VERSION}"

GTEST_OUTPUT_ENV_VAR = "GTEST_OUTPUT"

# Ex: if the exercise is "ex_0001", the binary will be named "ex_0001_TEST".
EXERCISE_PREFIX = "ex_"
TEST_BINARY_SUFFIX = "_TEST"
WINDOWS_BINARY_SUFFIX = ".exe"

EXERCISE_FOLDER_NAME = "Exercises"
UNIT_TESTS_FOLDER_NAME = "unitTests"
LEARNING_PATHS_FOLDER_NAME = "learningPaths"
BUILD_FOLDER_NAME = "BUILD"
ARGOS_FOLDER_NAME = ".argos"
CLI_FOLDER_NAME = "cli"
ROOT_CONFIG_FILE_NAME = ".argos-config.json"
STUDENT_REPOS_FOLDER_NAME = "students"
CLASSES_FOLDER_NAME = "classes"
HOOKS_FOLDER_NAME = "hooks"

SECTION_BEGIN_TEMPLATE = "//@ {name}:BEGIN"
SECTION_END_TEMPLATE = "//@ {name}:END"

SOLUTION_SECTION_NAME = "SOLUTION"
TODO_SECTION_NAME = "TODO"

ARGOS_HTTP_GITHUB_URL_TEMPLATE = "https://github.com/{username}/ARGOS.git"
ARGOS_SSH_GITHUB_URL_TEMPLATE = "git@github.com:{username}/ARGOS.git"

POSSIBLE_EXERCISE_EXTENSIONS = [".c", ".cpp"]

DIFFICULTY_POINTS: dict[str, int] = {"easy": 1, "medium": 2, "hard": 5}

METADATA_FILE_NAME = "metadata.json"
# These files are not considered when synchronizing exercises between the bank and the workspace.
SYNC_FILES_TO_IGNORE = [METADATA_FILE_NAME]


def _get_root_folder() -> str:
    if getattr(sys, "frozen", False):
        # Running as a PyInstaller executable placed at ROOT_FOLDER/argos.exe
        return path.abspath(Path(sys.executable).parent)
    return path.abspath(path.join(Path(__file__).parent, "../../.."))


ROOT_FOLDER = _get_root_folder()
ARGOS_FOLDER = path.join(ROOT_FOLDER, ARGOS_FOLDER_NAME)
CLI_FOLDER = path.join(ARGOS_FOLDER, CLI_FOLDER_NAME)

LOG_FILE_PATH = path.join(ARGOS_FOLDER, "argos.log")

ROOT_CONFIG_PATH = path.join(ROOT_FOLDER, ROOT_CONFIG_FILE_NAME)

EXERCISE_FOLDER_PATH = path.join(ROOT_FOLDER, EXERCISE_FOLDER_NAME)
LEARNING_PATHS_FOLDER_PATH = path.join(ARGOS_FOLDER, LEARNING_PATHS_FOLDER_NAME)
BUILD_FOLDER_PATH = path.join(ROOT_FOLDER, BUILD_FOLDER_NAME)
UNIT_TESTS_FOLDER_PATH = path.join(ARGOS_FOLDER, UNIT_TESTS_FOLDER_NAME)

BANK_EXERCISES_PATH = path.join(ARGOS_FOLDER, "exercises")
STUDENT_REPOS_FOLDER_PATH = path.join(ARGOS_FOLDER, STUDENT_REPOS_FOLDER_NAME)
CLASSES_FOLDER_PATH = path.join(ARGOS_FOLDER, CLASSES_FOLDER_NAME)
HOOKS_FOLDER_PATH = path.join(ARGOS_FOLDER, HOOKS_FOLDER_NAME)

SYNC_BASE_FOLDER_NAME = "sync_base"
SYNC_BASE_PATH = path.join(ARGOS_FOLDER, SYNC_BASE_FOLDER_NAME, EXERCISE_FOLDER_NAME)

DASHBOARDS_FOLDER_PATH = path.join(ARGOS_FOLDER, "dashboards")

DASHBOARD_FOLDER_PATH = path.join(DASHBOARDS_FOLDER_PATH, "student")
DASHBOARD_DATA_FILE_PATH = path.join(DASHBOARD_FOLDER_PATH, "data.js")
DASHBOARD_INDEX_FILE_PATH = path.join(DASHBOARD_FOLDER_PATH, "index.html")

ADMIN_DASHBOARD_FOLDER_PATH = path.join(DASHBOARDS_FOLDER_PATH, "admin")
ADMIN_DASHBOARD_DATA_FILE_PATH = path.join(ADMIN_DASHBOARD_FOLDER_PATH, "data.js")
ADMIN_DASHBOARD_INDEX_FILE_PATH = path.join(ADMIN_DASHBOARD_FOLDER_PATH, "index.html")
