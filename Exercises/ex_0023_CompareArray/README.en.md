<!-- Generated at publication from metadata.json — do not edit by hand -->

# 0023 — Compare Array

**Language:** C

**Difficulty:** 🟢 easy

**Tested skills:**
- 1D arrays

## Task

Implement **`ex_0023_CompareArray`** so that it compares the first
**`nb_vals`** elements of two integer arrays and returns **`true`** if
they are identical, **`false`** otherwise.

## Signature

**`ex_0023_CompareArray`** takes three parameters, in this order: two
**`int`** arrays **`array1`** and **`array2`**, and an **`int`**
**`nb_vals`**, the number of elements to compare. It returns a
**`bool`**.

## Examples

For the following arrays:

```c
int array1[] = {1, 2, 3, 4, 4};
int array2[] = {1, 2, 3, 4, 5};
```

| Call                                          | returned value |
|-----------------------------------------------|----------------|
| **`ex_0023_CompareArray(array1, array2, 0)`** | true           |
| **`ex_0023_CompareArray(array1, array2, 4)`** | true           |
| **`ex_0023_CompareArray(array1, array2, 5)`** | false          |
