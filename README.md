# ARGOS

ARGOS is a bank of C programming exercises with automated tests. You work on
the exercises locally, and the `argos` CLI compiles your code, runs the tests
and shows your progress on a dashboard.

## Prerequisites

`gcc` (with `g++`) is already installed on your machine. To check your
exercises, the `argos` CLI also needs:

- **CMake** ≥ 3.25 — <https://cmake.org/download/>
- **Ninja** — <https://github.com/ninja-build/ninja/releases>

Install both and make sure they are on your `PATH`. Check with:

```powershell
cmake --version
ninja --version
```

The first `check` downloads GoogleTest, so you need an internet connection
the first time.

Python is optional on Windows: it is only needed to run `argos.py` instead
of `argos.exe`. On Linux/macOS, you need Python ≥ 3.12.

## Getting started

1. **Fork this repository** (button at the top of this page) — every student
   works on their own fork, named `<your-login>/ARGOS`.
2. **Clone your fork**:

   ```bash
   git clone https://github.com/<your-login>/ARGOS.git
   cd ARGOS
   ```

3. **Activate your learning path** (your teacher gives you its id):

   ```powershell
   .\argos.exe learning-path add <learning-path-id>
   ```

   This copies the exercises of the learning path into the `Exercises/`
   folder — that is where you work.

   Example, for the HE-Arc 1242.1 C course:

   ```powershell
   .\argos.exe learning-path add HE-Arc_1242.1_C
   ```

## Doing an exercise

1. Pick an exercise from the catalogue below and read its statement (the
   `README.fr.md` / `README.en.md` files linked in the table).
2. Edit the exercise source in `Exercises/ex_NNNN_Name/` — each exercise
   tells you which function to write. The `main.c` next to it is a free
   sandbox: use it to call your function and test it by hand.

   Example, for exercise 0001: write the body of `ex_0001_PrintHelloWorld`
   in `Exercises/ex_0001_PrintHelloWorld/ex_0001_PrintHelloWorld.c`.
3. Compile by hand, from the exercise folder, with the course command:

   ```powershell
   cd Exercises/ex_NNNN_Name
   gcc -Wall -Wextra -Wpedantic -Werror -std=c23 -o main.exe main.c ex_NNNN_Name.c
   ```

   Fix every error and warning until it compiles, then run your program:

   ```powershell
   .\main.exe
   ```

   Try several inputs and compare with what the statement expects.

   Example, for exercise 0001:

   ```powershell
   cd Exercises/ex_0001_PrintHelloWorld
   gcc -Wall -Wextra -Wpedantic -Werror -std=c23 -o main.exe main.c ex_0001_PrintHelloWorld.c
   .\main.exe
   ```

   The program prints `hello, world`.
4. Only once your code compiles and you have tested it, check your solution
   from the project root. On Windows:

   ```powershell
   .\argos.exe check <exercise-id>
   ```

   On Linux/macOS (Python ≥ 3.12):

   ```bash
   python argos.py check <exercise-id>
   ```

   Example, for exercise 0001 (back at the project root):

   ```powershell
   cd ../..
   .\argos.exe check 0001
   ```

   Without an id, `check` runs every exercise of your selected learning
   paths. Each exercise earns points based on its difficulty (easy = 1,
   medium = 2, hard = 5); a series is completed when you reach its points
   target — you do not need to solve every exercise.

When your teacher updates the exercises, pull the changes from this
repository into your fork, then run `.\argos.exe sync` (a `git pull` also
triggers it automatically).

## Reading from stdin

When a statement asks you to flush `stdin` after a `scanf`, read and discard
every character left on the line, up to and including the newline `\n`, or
until `EOF` if the input ends first. Combined with input error handling (ask
again until the expected values are read), it looks like this:

```c
int status = 0;
const int nbExpectedValues = 1;
int x = 0;
do
{
  printf("Please enter an integer: ");
  status = scanf("%d", &x);

  {
    int c;
    do
    {
      c = getchar();
    } while (c != '\n' && c != EOF);
  }
} while (status != nbExpectedValues && status != EOF);
```

- `c` must be an `int`, not a `char`: otherwise the comparison with `EOF` may
  never be true.
- `status != EOF` covers a rare case: the input is over, not just empty. On
  an empty keyboard input, `scanf` waits for the user. But once the input has
  ended (the user typed Ctrl+Z then Enter on Windows, Ctrl+D on Linux/macOS,
  or the input comes from a file that has been read to the end, as in the
  tests), `scanf` returns `EOF` at once, every time. Without this check, the
  loop would print the prompt forever. When the loop stops on `EOF`, `x` was
  not read.
- Do not use `fflush(stdin)`: `fflush` is defined for output streams only, its
  behaviour on `stdin` depends on the platform.

Without this flush, what `scanf` left behind (the `\n`, or a token it could not
convert) is read again by the next read: the tests then fail, or never end.

## Dashboard

Every `check` updates your dashboard, a local web page showing your total
progression and your points per series. Its path is printed at the end of
`check` (ctrl+click to open it):

```text
Dashboard (ctrl+click to open): <project>\.argos\dashboards\student\index.html
```

Keep it open while you work: it refreshes by itself after each `check`.

![Student dashboard](docs/dashboard.png)

## Exercises

<!-- CATALOGUE:BEGIN -->
| ID | Exercise | Tested skills | Difficulty |
|----|----------|---------------|------------|
| 0001 | [Print Hello World](.argos/exercises/ex_0001_PrintHelloWorld/README.en.md) · [fr](.argos/exercises/ex_0001_PrintHelloWorld/README.fr.md) | basics | 🟢 easy |
| 0002 | [Print Math Calc](.argos/exercises/ex_0002_PrintMathCalc/README.en.md) · [fr](.argos/exercises/ex_0002_PrintMathCalc/README.fr.md) | arithmetic operators | 🟢 easy |
| 0003 | [Some Calculus](.argos/exercises/ex_0003_SomeCalculus/README.en.md) · [fr](.argos/exercises/ex_0003_SomeCalculus/README.fr.md) | arithmetic operators, variables and types | 🟢 easy |
| 0004 | [Swap](.argos/exercises/ex_0004_Swap/README.en.md) · [fr](.argos/exercises/ex_0004_Swap/README.fr.md) | variables and types | 🟢 easy |
| 0005 | [Celsius to Fahrenheit](.argos/exercises/ex_0005_CelsiusToFahrenheit/README.en.md) · [fr](.argos/exercises/ex_0005_CelsiusToFahrenheit/README.fr.md) | arithmetic operators | 🟢 easy |
| 0006 | [Asset Interest Rate](.argos/exercises/ex_0006_AssetInterestRate/README.en.md) · [fr](.argos/exercises/ex_0006_AssetInterestRate/README.fr.md) | arithmetic operators, variables and types | 🟡 medium |
| 0007 | [Printf](.argos/exercises/ex_0007_Printf/README.en.md) · [fr](.argos/exercises/ex_0007_Printf/README.fr.md) | formatted input/output | 🟢 easy |
| 0008 | [Scanf Printf](.argos/exercises/ex_0008_ScanfPrintf/README.en.md) · [fr](.argos/exercises/ex_0008_ScanfPrintf/README.fr.md) | formatted input/output | 🟢 easy |
| 0009 | [Circle](.argos/exercises/ex_0009_Circle/README.en.md) · [fr](.argos/exercises/ex_0009_Circle/README.fr.md) | formatted input/output | 🟡 medium |
| 0010 | [Lowercase Uppercase](.argos/exercises/ex_0010_LowercaseUppercase/README.en.md) · [fr](.argos/exercises/ex_0010_LowercaseUppercase/README.fr.md) | conditionals (if / switch) | 🟡 medium |
| 0011 | [Multiplication Sign](.argos/exercises/ex_0011_MultiplicationSign/README.en.md) · [fr](.argos/exercises/ex_0011_MultiplicationSign/README.fr.md) | conditionals (if / switch) | 🟡 medium |
| 0012 | [Decreasing Output](.argos/exercises/ex_0012_DecreasingOutput/README.en.md) · [fr](.argos/exercises/ex_0012_DecreasingOutput/README.fr.md) | conditionals (if / switch) | 🟢 easy |
| 0013 | [Second Order Equation](.argos/exercises/ex_0013_SecondOrderEquation/README.en.md) · [fr](.argos/exercises/ex_0013_SecondOrderEquation/README.fr.md) | conditionals (if / switch) | 🟡 medium |
| 0014 | [Currency Converter](.argos/exercises/ex_0014_CurrencyConverter/README.en.md) · [fr](.argos/exercises/ex_0014_CurrencyConverter/README.fr.md) | conditionals (if / switch) | 🟡 medium |
| 0015 | [Days In Month](.argos/exercises/ex_0015_DaysInMonth/README.en.md) · [fr](.argos/exercises/ex_0015_DaysInMonth/README.fr.md) | conditionals (if / switch) | 🟡 medium |
| 0016 | [Sum Product Mean](.argos/exercises/ex_0016_SumProductMean/README.en.md) · [fr](.argos/exercises/ex_0016_SumProductMean/README.fr.md) | for loop, formatted input/output | 🔴 hard |
| 0017 | [Factorial](.argos/exercises/ex_0017_Factorial/README.en.md) · [fr](.argos/exercises/ex_0017_Factorial/README.fr.md) | for loop | 🟢 easy |
| 0018 | [Squares](.argos/exercises/ex_0018_Squares/README.en.md) · [fr](.argos/exercises/ex_0018_Squares/README.fr.md) | for loop, functions (pass by value) | 🟢 easy |
| 0019 | [Multiplication Table](.argos/exercises/ex_0019_MultiplicationTable/README.en.md) · [fr](.argos/exercises/ex_0019_MultiplicationTable/README.fr.md) | for loop, functions (pass by value) | 🟢 easy |
| 0020 | [Calculator](.argos/exercises/ex_0020_Calculator/README.en.md) · [fr](.argos/exercises/ex_0020_Calculator/README.fr.md) | conditionals (if / switch), functions (pass by value) | 🟡 medium |
| 0021 | [Sum N](.argos/exercises/ex_0021_SumN/README.en.md) · [fr](.argos/exercises/ex_0021_SumN/README.fr.md) | for loop, functions (pass by value) | 🟢 easy |
| 0022 | [Invert](.argos/exercises/ex_0022_Invert/README.en.md) · [fr](.argos/exercises/ex_0022_Invert/README.fr.md) | while loop, functions (pass by value) | 🟡 medium |
| 0023 | [Compare Array](.argos/exercises/ex_0023_CompareArray/README.en.md) · [fr](.argos/exercises/ex_0023_CompareArray/README.fr.md) | 1D arrays | 🟢 easy |
| 0024 | [Print Array](.argos/exercises/ex_0024_PrintArray/README.en.md) · [fr](.argos/exercises/ex_0024_PrintArray/README.fr.md) | 1D arrays | 🟢 easy |
<!-- CATALOGUE:END -->

## License

ARGOS — the CLI, tests, exercise statements and skeletons — is released under
the [MIT License](LICENSE).
