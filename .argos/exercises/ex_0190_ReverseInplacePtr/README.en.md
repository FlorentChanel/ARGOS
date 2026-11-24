<!-- Generated at publication from metadata.json — do not edit by hand -->

# 0190 — Reverse Inplace Ptr

**Language:** C

**Difficulty:** 🟢 easy

**Tested skills:**
- pointer arithmetic

## Task

Implement **`ex_0190_ReverseInplacePtr`** so that it reverses the order of the
elements of an array of integers, in place: the array itself is modified, no
other array is used, by moving two pointers towards each other.

## Signature

**`ex_0190_ReverseInplacePtr`** takes two parameters: **`array`** of type
pointer to an **`int`** (the first element of the array to reverse) and
**`size`** of type **`int`** (the number of elements of the array). It returns
nothing.

## Examples

```c
int array[] = {1, 2, 3, 4, 5};
ex_0190_ReverseInplacePtr(array, 5);
```

**`array`** is now **`{5, 4, 3, 2, 1}`**.

```c
int array[] = {-3, 8, 0, 12};
ex_0190_ReverseInplacePtr(array, 4);
```

**`array`** is now **`{12, 0, 8, -3}`**.

```c
int array[] = {7, 7, 2};
ex_0190_ReverseInplacePtr(array, 3);
```

**`array`** is now **`{2, 7, 7}`**.

```c
int array[] = {42};
ex_0190_ReverseInplacePtr(array, 1);
```

**`array`** is still **`{42}`**.

## Constraints

- **`size`** is at least **`1`**.
- Do not use the **`[]`** operator.
