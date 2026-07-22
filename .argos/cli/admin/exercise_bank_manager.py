import re
from pathlib import Path

from config.models import ExerciseLanguage
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

    def create(
        self, slug: str, language: ExerciseLanguage = ExerciseLanguage.C
    ) -> tuple[Path, Path]:
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
        ext = ".c" if language == ExerciseLanguage.C else ".cpp"
        lang_value = language.value

        (exercise_dir / f"{fullname}{ext}").write_text(
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

        if language == ExerciseLanguage.C:
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
        else:
            (exercise_dir / "main.cpp").write_text(
                "// Author: HE-Arc\n"
                "\n"
                "// Standard includes\n"
                "#include <iostream>\n"
                "\n"
                "// Local includes\n"
                f'#include "{fullname}.h"\n'
                "\n"
                "int main()\n"
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
            f'  "language": "{lang_value}",\n'
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
            f"```{lang_value}\n"
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
            f"```{lang_value}\n"
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

        exercise_include = ('extern "C"\n'
                        "{\n"
                        f'  #include "../../../Exercises/{fullname}/{fullname}.c"\n'
                        "}\n")

        if language == ExerciseLanguage.CPP:
            exercise_include = f'#include "../../../Exercises/{fullname}/{fullname}.cpp"\n'

        unit_test_content = (
            f"{exercise_include}"
            "\n"
            "#include <gtest/gtest.h>\n"
            "\n"
            '#include "Common/Utils.h"\n'
            "\n"
            f"TEST({test_name}, {slug})\n"
            "{\n"
            f"  // TODO: implement the tests for {fullname}\n"
            "  EXPECT_EQ(1, 1);\n"
            "}\n"
        )

        (unit_test_dir / f"{binary_name}.cpp").write_text(
            unit_test_content, encoding="utf-8"
        )

        return exercise_dir, unit_test_dir
