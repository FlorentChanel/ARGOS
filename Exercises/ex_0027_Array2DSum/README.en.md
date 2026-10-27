<!-- Generated at publication from metadata.json — do not edit by hand -->

# 0027 — Array 2D Sum

**Language:** C

**Difficulty:** 🔴 hard

**Tested skills:**
- 2D arrays / matrices
- formatted input/output

## Task

Implement **`ex_0027_Array2DSum`** so that it:

1. declares an integer array (maximum size: 50 lines and 50 columns)
2. reads the sizes (number of lines and number of columns) from the
   keyboard
3. fills the array with values entered on the keyboard
4. prints the sum of all its elements

## Signature

**`ex_0027_Array2DSum`** takes no parameters and returns nothing (**`void`**).

## Examples

In the examples, the text after each prompt is typed by the user; each prompt
ends with one space and no newline.

```
Nb lines (max.50): a
Nb lines (max.50): -1
Nb lines (max.50): 2
Nb columns (max.50): a
Nb columns (max.50): -1
Nb columns (max.50): 2
array[0][0]: 1
array[0][1]: 2
array[1][0]: 3
array[1][1]: 4
Total sum: 10
```

```
Nb lines (max.50): 0
Nb columns (max.50): 9
Total sum: 0
```

```
Nb lines (max.50): 9
Nb columns (max.50): 0
Total sum: 0
```

```
Nb lines (max.50): 0
Nb columns (max.50): 0
Total sum: 0
```

## Constraints

- Handle input errors: keep prompting with the same prompt until a valid size
  or value is read.
- A valid size is an integer from 0 to 50 inclusive.
- After each **`scanf`**, flush **`stdin`**: discard the rest of the line, up to
  **`\n`** or **`EOF`** (see [Reading from stdin](https://github.com/HE-Arc/ARGOS#reading-from-stdin)).
- The output ends with a newline.
