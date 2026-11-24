<!-- Generated at publication from metadata.json — do not edit by hand -->

# 0032 — Copy Arrays

**Language:** C

**Difficulty:** 🟡 medium

**Tested skills:**
- pass by address
- 1D arrays

## Task

Implement **`ex_0032_CopyArrays`** so that it copies the first **`n`** elements
of a source integer array into a destination integer array. The source array is
not modified, and the elements of the destination array beyond the first
**`n`** are left unchanged.

## Signature

**`ex_0032_CopyArrays`** takes three parameters, in this order: the source
array **`src`** (pointer to a **`const int`**), the destination array **`dst`**
(pointer to an **`int`**) and the number of elements to copy **`n`**
(**`int`**). It returns nothing.

## Examples

```c
int src[] = {4, -1, 7, 0, 12};
int dst[] = {0, 0, 0, 0, 0};
ex_0032_CopyArrays(src, dst, 5);
```

**`dst`** is now **`{4, -1, 7, 0, 12}`** and **`src`** is still
**`{4, -1, 7, 0, 12}`**.

```c
int src[] = {9, 8, 7, 6};
int dst[] = {1, 1, 1, 1, 1, 1};
ex_0032_CopyArrays(src, dst, 3);
```

**`dst`** is now **`{9, 8, 7, 1, 1, 1}`**.

```c
int src[] = {5, 5};
int dst[] = {3, 3};
ex_0032_CopyArrays(src, dst, 0);
```

**`dst`** is still **`{3, 3}`**.

## Constraints

- **`n`** is at least 0 and both arrays have at least **`n`** elements.
- The two arrays do not overlap.
