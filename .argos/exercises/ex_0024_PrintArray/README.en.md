<!-- Generated at publication from metadata.json — do not edit by hand -->

# 0024 — Print Array

**Language:** C

**Difficulty:** 🟢 easy

**Tested skills:**
- 1D arrays

## Task

Implement **`ex_0024_PrintArray`** so that it prints an integer array on
the screen.

## Signature

**`ex_0024_PrintArray`** takes two parameters, in this order: an
**`int`** array **`array`** and an **`int`** **`size`**, the number of
elements of the array. It returns nothing (**`void`**).

## Examples

For the following array:

```c
int array[] = {1, 2, 3, 4, 5};
```

| Call                                | output          |
|-------------------------------------|-----------------|
| **`ex_0024_PrintArray(array, 0)`**  | *nothing*       |
| **`ex_0024_PrintArray(array, 4)`**  | **`1 2 3 4`**   |
| **`ex_0024_PrintArray(array, 5)`**  | **`1 2 3 4 5`** |

> [!WARNING]
> Each array element is followed by a space, **except the last one**.
> Moreover, the output must **not** end with a **`\n`**.
