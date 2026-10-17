<!-- Generated at publication from metadata.json — do not edit by hand -->

# 0017 — Factorial

**Language:** C

**Difficulty:** 🟢 easy

**Tested skills:**
- for loop

## Task

Complete **`ex_0017_Factorial`** so that it reads a non-negative integer $N$,
then computes and prints its factorial $N!$ such that:

$$N! = 1 \times 2 \times 3 \times \dots \times (N-1) \times N$$

and

$$0! = 1$$

## Signature

```c
void ex_0017_Factorial(void);
```

## Examples

```
Please enter a non-negative integer N: 6
6! = 720
```

```
Please enter a non-negative integer N: 0
0! = 1
```

```
Please enter a non-negative integer N: -1
Please enter a non-negative integer N: a
Please enter a non-negative integer N: 6
6! = 720
```

## Constraints

- Compute $N!$ with a loop (no recursion).
- Handle input errors: keep prompting until a non-negative integer is read.
- The printed result must be exact for every $N$ from **`0`** to **`20`**.
- After each **`scanf`**, flush **`stdin`**: discard the rest of the line, up to
  **`\n`** or **`EOF`** (see [Reading from stdin](https://github.com/HE-Arc/ARGOS#reading-from-stdin)).
- The output ends with a newline.
