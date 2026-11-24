<!-- Generated at publication from metadata.json — do not edit by hand -->

# 0188 — Reverse Array Ptr

**Language:** C

**Difficulty:** 🟡 medium

**Tested skills:**
- pointers / dereferencing

## Task

Implement **`ex_0188_ReverseArrayPtr`** so that it copies the elements of an
array of integers into a second array, in reverse order. The source array is
left unchanged.

## Signature

**`ex_0188_ReverseArrayPtr`** takes three parameters: **`source`** of type
pointer to a constant **`int`** (the first element of the array to copy),
**`destination`** of type pointer to an **`int`** (the first element of the
array that receives the copy), and **`size`** of type **`int`** (the number of
elements of each array). It returns nothing.

## Examples

```c
int source[] = {1, 2, 3, 4, 5};
int destination[5];
ex_0188_ReverseArrayPtr(source, destination, 5);
```

**`destination`** is now **`{5, 4, 3, 2, 1}`** and **`source`** is still
**`{1, 2, 3, 4, 5}`**.

```c
int source[] = {-3, 8, 0, 12};
int destination[4];
ex_0188_ReverseArrayPtr(source, destination, 4);
```

**`destination`** is now **`{12, 0, 8, -3}`**.

```c
int source[] = {7, 7, 2};
int destination[3];
ex_0188_ReverseArrayPtr(source, destination, 3);
```

**`destination`** is now **`{2, 7, 7}`**.

```c
int source[] = {42};
int destination[1];
ex_0188_ReverseArrayPtr(source, destination, 1);
```

**`destination`** is now **`{42}`**.

## Constraints

- **`size`** is at least **`1`**.
- **`source`** and **`destination`** do not overlap.
