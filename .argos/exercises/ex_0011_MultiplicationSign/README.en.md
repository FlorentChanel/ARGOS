<!-- Generated at publication from metadata.json — do not edit by hand -->

# 0011 — Multiplication Sign

**Language:** C

**Difficulty:** 🟡 medium

**Tested skills:**
- conditionals (if / switch)

## Task

Complete **`ex_0011_MultiplicationSign`** so that it reads two integer
values (**`a`** and **`b`**) from the keyboard and prints the sign of the
product of **`a`** and **`b`** (positive, negative or zero) **without
computing the multiplication**.

## Signature

```c
void ex_0011_MultiplicationSign(void);
```

## Examples

```
Please enter 2 integers: 1 2
1 * 2 > 0
```

```
Please enter 2 integers: 0 0
0 * 0 = 0
```

```
Please enter 2 integers: a b
Please enter 2 integers: b 1
Please enter 2 integers: -1 3
-1 * 3 < 0
```

## Constraints

- Handle input errors: keep prompting until two integers are read.
- After each **`scanf`**, flush **`stdin`**: discard the rest of the line, up to
  **`\n`** or **`EOF`** (see [Reading from stdin](https://github.com/HE-Arc/ARGOS#reading-from-stdin)).
- The output ends with a newline.
