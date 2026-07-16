import re
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

    def create(self, slug: str) -> tuple[Path, Path]:
        """Scaffolds a new exercise (regime A) matching the frozen bank structure."""
        exercise_id = self.next_id()
        fullname = f"{EXERCISE_PREFIX}{exercise_id}_{slug}"
        test_name = f"{EXERCISE_PREFIX}{exercise_id}"
        binary_name = test_name + TEST_BINARY_SUFFIX

        exercise_dir = Path(BANK_EXERCISES_PATH) / fullname
        unit_test_dir = Path(UNIT_TESTS_FOLDER_PATH) / fullname

        if exercise_dir.exists() or unit_test_dir.exists():
            raise FileExistsError(f"Exercise '{fullname}' already exists in the bank.")

        exercise_dir.mkdir(parents=True)
        unit_test_dir.mkdir(parents=True)

        header_guard = f"{fullname.upper()}_H"
        display_name = re.sub(r"(?<!^)(?=[A-Z])", " ", slug)

        (exercise_dir / f"{fullname}.c").write_text(
            "// Author: HE-Arc\n"
            "\n"
            "// Standard includes\n"
            "\n"
            "// Local includes\n"
            f'#include "{fullname}.h"\n'
            "\n"
            "// Function definitions\n"
            f"void {fullname}(void)\n"
            "{\n"
            "  // TODO\n"
            "  //@ SOLUTION:BEGIN\n"
            "  //@ SOLUTION:END\n"
            "}\n",
            encoding="utf-8",
        )

        (exercise_dir / f"{fullname}.h").write_text(
            "// Author: HE-Arc\n"
            "\n"
            f"#ifndef {header_guard}\n"
            f"#define {header_guard}\n"
            "\n"
            "// Standard includes\n"
            "\n"
            "// Local includes\n"
            "\n"
            "// Function prototypes\n"
            f"void {fullname}(void);\n"
            "\n"
            f"#endif // {header_guard}\n",
            encoding="utf-8",
        )

        (exercise_dir / "main.c").write_text(
            "// Author: HE-Arc\n"
            "\n"
            "// Standard includes\n"
            "#include <stdio.h>\n"
            "\n"
            "// Local includes\n"
            f'#include "{fullname}.h"\n'
            "\n"
            "int main(void)\n"
            "{\n"
            f"  {fullname}();\n"
            "\n"
            "  return 0;\n"
            "}\n",
            encoding="utf-8",
        )

        (exercise_dir / METADATA_FILE_NAME).write_text(
            "{\n"
            '  "$schema": "../metadata.schema.json",\n'
            f'  "name": "{display_name}",\n'
            '  "description": "TODO",\n'
            '  "difficulty": "easy",\n'
            '  "language": "c",\n'
            '  "skills": []\n'
            "}\n",
            encoding="utf-8",
        )

        (exercise_dir / "README.en.md").write_text(
            "## Task\n"
            "\n"
            f"Complete **`{fullname}`** so that it… <!-- TODO -->\n"
            "\n"
            "## Signature\n"
            "\n"
            "```c\n"
            f"void {fullname}(void);\n"
            "```\n"
            "\n"
            "## Expected output\n"
            "\n"
            "<!-- TODO -->\n"
            "\n"
            "## Constraints\n"
            "\n"
            "<!-- TODO: fill in, or remove this section if empty -->\n",
            encoding="utf-8",
        )

        (exercise_dir / "README.fr.md").write_text(
            "## Tâche\n"
            "\n"
            f"Complétez **`{fullname}`** pour qu'elle… <!-- TODO -->\n"
            "\n"
            "## Signature\n"
            "\n"
            "```c\n"
            f"void {fullname}(void);\n"
            "```\n"
            "\n"
            "## Sortie attendue\n"
            "\n"
            "<!-- TODO -->\n"
            "\n"
            "## Contraintes\n"
            "\n"
            "<!-- TODO: fill in, or remove this section if empty -->\n",
            encoding="utf-8",
        )

        (unit_test_dir / f"{binary_name}.cpp").write_text(
            'extern "C"\n'
            "{\n"
            f'  #include "../../../Exercises/{fullname}/{fullname}.c"\n'
            "}\n"
            "\n"
            "#include <gtest/gtest.h>\n"
            "\n"
            '#include "Common/Utils.h"\n'
            "\n"
            f"TEST({test_name}, {slug})\n"
            "{\n"
            f"  // TODO: implement the tests for {fullname}\n"
            "  EXPECT_EQ(1, 1);\n"
            "}\n",
            encoding="utf-8",
        )

        # Still required by the root CMakeLists (add_subdirectory loop);
        # drop this file when the centralized CMake generation lands.
        (unit_test_dir / "CMakeLists.txt").write_text(
            f"add_executable({binary_name} {binary_name}.cpp)\n"
            "\n"
            f"target_link_libraries({binary_name} argos_common GTest::gtest_main)\n"
            "\n"
            "include(GoogleTest)\n"
            "\n"
            f"gtest_discover_tests({binary_name} EXTRA_ARGS --gtest_color=1)\n"
            "\n"
            f"if(EXISTS ${{CMAKE_CURRENT_SOURCE_DIR}}/../../../Exercises/{fullname}/main.c)\n"
            "  # With a header the exercise uses separate compilation; without it, main.c includes the .c\n"
            f"  if(EXISTS ${{CMAKE_CURRENT_SOURCE_DIR}}/../../../Exercises/{fullname}/{fullname}.h)\n"
            f"    add_executable({test_name} ../../../Exercises/{fullname}/main.c ../../../Exercises/{fullname}/{fullname}.c)\n"
            "  else()\n"
            f"    add_executable({test_name} ../../../Exercises/{fullname}/main.c)\n"
            "  endif()\n"
            "endif()\n",
            encoding="utf-8",
        )

        return exercise_dir, unit_test_dir
