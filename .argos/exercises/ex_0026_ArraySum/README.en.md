<!-- Generated at publication from metadata.json — do not edit by hand -->

# 0026 — Array Sum

**Language:** C

**Difficulty:** 🟢 easy

**Tested skills:**
- 1D arrays
- for loop

## Task

Implement **`ex_0026_ArraySum`** so that it:

1. declares an array able to hold at most 50 integers
2. asks the user for the number of values **`n`** to enter (maximum 50)
3. fills the array with **`n`** values entered on the keyboard
4. prints the first **`n`** elements of the array
5. prints the sum of the entered values stored in the array

## Signature

**`ex_0026_ArraySum`** takes no parameters and returns nothing (**`void`**).

## Examples

In the examples, the text after each prompt is typed by the user; each prompt
ends with one space and no newline.

```
Nb values (max.50): a
Nb values (max.50): b
Nb values (max.50): -2
Nb values (max.50): -1
Nb values (max.50): 0
array:

Total sum: 0
```

```
Nb values (max.50): 4
Value 0? -2
Value 1? -1
Value 2? 0
Value 3? 1
array:
-2 -1 0 1
Total sum: -2
```

## Constraints

- Handle input errors: **`n`** is valid from 0 to 50, any other entry prints
  the **`Nb values (max.50): `** prompt again.
- An invalid entry at a **`Value i? `** prompt is discarded and the same
  **`Value i? `** prompt is printed again.
- The values of the array are printed on one line, separated by one space, with
  no trailing space, then a newline.
- After each **`scanf`**, flush **`stdin`**: discard the rest of the line, up to
  **`\n`** or **`EOF`** (see [Reading from stdin](https://github.com/HE-Arc/ARGOS#reading-from-stdin)).
- The output ends with a newline.
