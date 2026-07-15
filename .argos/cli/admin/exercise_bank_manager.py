from pathlib import Path

from git_bindings import GitBindings
from utils.constants import (
    BANK_EXERCISES_PATH,
    EXERCISE_PREFIX,
    METADATA_FILE_NAME,
    TEST_BINARY_SUFFIX,
    UNIT_TESTS_FOLDER_PATH,
)


class ExerciseBankManager:
    def __init__(self, git_bindings: GitBindings):
        self._git_bindings = git_bindings

    def next_id(self) -> str:
        ids: list[int] = []
        for p in Path(BANK_EXERCISES_PATH).iterdir():
            if p.is_dir():
                parts = p.name.split("_")
                if len(parts) >= 3 and parts[0] == "ex" and parts[1].isdigit():
                    ids.append(int(parts[1]))
        return str((max(ids) + 1) if ids else 1).zfill(4)

    def create(self, description: str) -> tuple[Path, Path]:
        exercise_id = self.next_id()
        fullname = f"{EXERCISE_PREFIX}{exercise_id}_{description}"
        test_name = f"{EXERCISE_PREFIX}{exercise_id}"
        binary_name = test_name + TEST_BINARY_SUFFIX

        exercise_dir = Path(BANK_EXERCISES_PATH) / fullname
        unit_test_dir = Path(UNIT_TESTS_FOLDER_PATH) / fullname

        if exercise_dir.exists() or unit_test_dir.exists():
            raise FileExistsError(f"Exercise '{fullname}' already exists in the bank.")

        exercise_dir.mkdir(parents=True)
        unit_test_dir.mkdir(parents=True)

        (exercise_dir / f"{fullname}.c").write_text(
            f"#include <stdio.h>\n\n"
            f"void {fullname}(void);\n\n"
            f"void {fullname}(void) {{\n"
            f"    // TODO: implement {fullname}\n"
            f"}}\n",
            encoding="utf-8",
        )

        (exercise_dir / "main.c").write_text(
            f'#include "{fullname}.c"\n\n'
            f"int main(void) {{\n"
            f"    {fullname}();\n"
            f"    return 0;\n"
            f"}}\n",
            encoding="utf-8",
        )

        (exercise_dir / METADATA_FILE_NAME).write_text(
            "{\n"
            f'   "$schema": "../metadata.schema.json",\n'
            f'   "name": "{fullname}",\n'
            '   "description": "TODO",\n'
            '   "difficulty": "TODO",\n'
            '   "language": "c",\n'
            '   "skills": []\n'
            "}\n",
            encoding="utf-8",
        )

        (unit_test_dir / f"{binary_name}.cpp").write_text(
            f'extern "C" {{\n'
            f'    #include "../../../Exercises/{fullname}/{fullname}.c"\n'
            f"}}\n\n"
            f"#include <gtest/gtest.h>\n\n"
            f'#include "Common/Utils.h"\n\n'
            f"TEST({test_name}, {description})\n"
            f"{{\n"
            f"    // TODO: implement test for {fullname}\n"
            f"    EXPECT_EQ(1, 1);\n"
            f"}}\n",
            encoding="utf-8",
        )

        (unit_test_dir / "CMakeLists.txt").write_text(
            f"add_executable({binary_name} {binary_name}.cpp)\n\n"
            f"target_link_libraries({binary_name} argos_common GTest::gtest_main)\n\n"
            f"include(GoogleTest)\n\n"
            f"gtest_discover_tests({binary_name} EXTRA_ARGS --gtest_color=1)\n\n"
            f"if(EXISTS ${{CMAKE_CURRENT_SOURCE_DIR}}/../../../Exercises/{fullname}/main.c)\n"
            f"  add_executable({test_name} ../../../Exercises/{fullname}/main.c)\n"
            f"endif()\n",
            encoding="utf-8",
        )

        return exercise_dir, unit_test_dir
