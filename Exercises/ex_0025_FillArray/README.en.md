<!-- Generated at publication from metadata.json — do not edit by hand -->

# 0025 — Fill Array

**Language:** C

**Difficulty:** 🟢 easy

**Tested skills:**
- 1D arrays
- formatted input/output

## Task

Implement **`ex_0025_FillArray`** so that it fills the integer array passed
as parameter with values entered on the keyboard by the user. Input stops
when the user enters a negative value, when the array holds
**`max_capacity`** values, or at the end of input; nothing is read when **`max_capacity`** is 0 or
negative. The function returns the number of correct values entered.

## Signature

**`ex_0025_FillArray`** takes two parameters, in this order: an **`int`**
array **`array`** and its **`int`** capacity **`max_capacity`**. It returns
an **`int`**.

## Examples

**`ex_0025_FillArray(array, -1)`** and **`ex_0025_FillArray(array, 0)`**
do nothing and return 0.

For the array:

```c
int array[] = {-2, -2, -2, -2};
```

**`ex_0025_FillArray(array, 4)`** with the keyboard inputs

```
a
b
1
-1
```

changes the array into **`{1, -2, -2, -2}`** and returns 1.

**`ex_0025_FillArray(array, 4)`** with the keyboard inputs

```
2
2
-2
```

changes the array into **`{2, 2, -2, -2}`** and returns 2.

**`ex_0025_FillArray(array, 4)`** with the keyboard inputs

```
3
3
-2
```

changes the array into **`{3, 3, -2, -2}`** and returns 2.

## Constraints

- Handle input errors: entries that are not numbers are ignored.
- After each **`scanf`**, flush **`stdin`**: discard the rest of the line, up to
  **`\n`** or **`EOF`** (see [Reading from stdin](https://github.com/HE-Arc/ARGOS#reading-from-stdin)).
