<!-- Generated at publication from metadata.json — do not edit by hand -->

# 0012 — Decreasing Output

**Language:** C

**Difficulty:** 🟢 easy

**Tested skills:**
- conditionals (if / switch)

## Task

Complete **`ex_0012_DecreasingOutput`** so that it prints in decreasing
order three numbers entered by the user. Exchange the contents of the
variables so that the first one holds the largest value, the second the
median and the third the smallest.

## Signature

```c
void ex_0012_DecreasingOutput(void);
```

## Examples

```
Please enter 3 integers separated by commas: 1,2,3
The 3 integers sorted in decreasing order: 3, 2, 1
```

```
Please enter 3 integers separated by commas: 1,-2,0
The 3 integers sorted in decreasing order: 1, 0, -2
```

```
Please enter 3 integers separated by commas: a,1,2
Please enter 3 integers separated by commas: 1, -9, c
Please enter 3 integers separated by commas: 0,0,0
The 3 integers sorted in decreasing order: 0, 0, 0
```

## Constraints

- The three integers are separated by commas; spaces are allowed before and
  after each comma (e.g. **`1 , -2,0`**). The rest of the line after the third
  integer is ignored.
- Handle input errors: keep prompting until three integers are read.
- After each **`scanf`**, flush **`stdin`**: discard the rest of the line, up to
  **`\n`** or **`EOF`** (see [Reading from stdin](https://github.com/HE-Arc/ARGOS#reading-from-stdin)).
- The output ends with a newline.
