# ARGOS

ARGOS is a bank of C programming exercises with automated tests. You work on
the exercises locally, and the `argos` CLI compiles your code, runs the tests
and shows your progress on a dashboard.

## Getting started

1. **Fork this repository** (button at the top of this page) — every student
   works on their own fork, named `<your-login>/ARGOS`.
2. **Clone your fork**:

   ```bash
   git clone https://github.com/<your-login>/ARGOS.git
   cd ARGOS
   ```

3. **Run the CLI.** On Windows, use the executable at the project root:

   ```powershell
   .\argos.exe
   ```

   On Linux/macOS, use the Python entry point instead (Python ≥ 3.12):

   ```bash
   python argos_cli.py
   ```

   Every command has a help option available with the `-h` flag. The examples
   below use `.\argos.exe`; substitute `python argos_cli.py` if needed.

4. **Activate your learning path** (your teacher gives you its id):

   ```powershell
   .\argos.exe learning-path add <learning-path-id>
   ```

   This copies the exercises of the learning path into the `Exercises/`
   folder — that is where you work.

## Doing an exercise

1. Pick an exercise from the catalogue below and read its statement (the
   `README.fr.md` / `README.en.md` files linked in the table).
2. Edit the exercise source in `Exercises/ex_NNNN_Name/` — each exercise
   tells you which function to complete. The `main.c` next to it is a free
   sandbox: use it to experiment by hand.
3. Check your solution:

   ```powershell
   .\argos.exe check <exercise-id>
   ```

   Without an id, `check` runs every exercise of your selected learning
   paths. Each exercise earns points based on its difficulty (easy = 1,
   medium = 2, hard = 5); a series is completed when you reach its points
   target — you do not need to solve every exercise.

When your teacher updates the exercises, pull the changes from this
repository into your fork, then run `.\argos.exe sync` (a `git pull` also
triggers it automatically).

## Exercises

<!-- CATALOGUE:BEGIN -->
| ID | Exercise | Tested skills | Difficulty |
|----|----------|---------------|------------|
| 0001 | [Print Hello World](.argos/exercises/ex_0001_PrintHelloWorld/README.en.md) · [fr](.argos/exercises/ex_0001_PrintHelloWorld/README.fr.md) | basics | 🟢 easy |
| 0002 | [Print Math Calc](.argos/exercises/ex_0002_PrintMathCalc/README.en.md) · [fr](.argos/exercises/ex_0002_PrintMathCalc/README.fr.md) | arithmetic operators | 🟢 easy |
| 0003 | [Some Calculus](.argos/exercises/ex_0003_SomeCalculus/README.en.md) · [fr](.argos/exercises/ex_0003_SomeCalculus/README.fr.md) | basics, arithmetic operators, variables and types | 🟢 easy |
| 0004 | [Swap](.argos/exercises/ex_0004_Swap/README.en.md) · [fr](.argos/exercises/ex_0004_Swap/README.fr.md) | basics, variables and types, formatted input/output | 🟢 easy |
| 0005 | [Celsius to Fahrenheit](.argos/exercises/ex_0005_CelsiusToFahrenheit/README.en.md) · [fr](.argos/exercises/ex_0005_CelsiusToFahrenheit/README.fr.md) | basics, arithmetic operators, formatted input/output | 🟢 easy |
| 0006 | [Asset Interest Rate](.argos/exercises/ex_0006_AssetInterestRate/README.en.md) · [fr](.argos/exercises/ex_0006_AssetInterestRate/README.fr.md) | basics, arithmetic operators, variables and types, formatted input/output | 🟡 medium |
<!-- CATALOGUE:END -->
