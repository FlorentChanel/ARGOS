<!-- Generated at publication from metadata.json — do not edit by hand -->

# 0192 — Array Slice

**Language:** C

**Difficulty:** 🟡 medium

**Tested skills:**
- pointer arithmetic

## Task

Implement **`ex_0192_ArraySlice`** so that it copies a slice of an array of
integers into a second array: the elements from index **`start`** included to
index **`end`** excluded, in the same order. It returns the number of elements
copied. The source array is left unchanged.

If the bounds are invalid (**`start`** negative, **`end`** greater than
**`size`**, or **`start`** greater than **`end`**), nothing is copied and the
function returns **`-1`**.

## Signature

**`ex_0192_ArraySlice`** takes five parameters: **`source`** of type pointer to
a constant **`int`** (the first element of the array to slice), **`size`** of
type **`int`** (the number of elements of **`source`**), **`start`** and
**`end`** of type **`int`** (the bounds of the slice), and **`destination`** of
type pointer to an **`int`** (the first element of the array that receives the
slice). It returns an **`int`**: the number of elements copied, or **`-1`**.

## Examples

```c
int source[] = {10, 20, 30, 40, 50, 60};
int destination[6];
int count = ex_0192_ArraySlice(source, 6, 1, 4, destination);
```

**`count`** is **`3`** and the first three elements of **`destination`** are
**`{20, 30, 40}`**. **`source`** is still **`{10, 20, 30, 40, 50, 60}`**.

```c
int source[] = {-5, 7, 0, 3};
int destination[4];
int count = ex_0192_ArraySlice(source, 4, 0, 4, destination);
```

**`count`** is **`4`** and **`destination`** is **`{-5, 7, 0, 3}`**.

```c
int source[] = {1, 2, 3, 4, 5};
int destination[5];
int count = ex_0192_ArraySlice(source, 5, 4, 5, destination);
```

**`count`** is **`1`** and the first element of **`destination`** is **`5`**.

```c
int source[] = {1, 2, 3};
int destination[3] = {9, 9, 9};
int count = ex_0192_ArraySlice(source, 3, 2, 2, destination);
```

**`count`** is **`0`** and **`destination`** is still **`{9, 9, 9}`**.

```c
int source[] = {1, 2, 3};
int destination[3] = {9, 9, 9};
int count = ex_0192_ArraySlice(source, 3, 1, 4, destination);
```

**`count`** is **`-1`** and **`destination`** is still **`{9, 9, 9}`**. The
same holds for **`start`** equal to **`-1`**, or for **`start`** equal to
**`2`** with **`end`** equal to **`1`**.

## Constraints

- **`size`** is at least **`1`**.
- **`destination`** holds at least **`size`** elements and does not overlap
  **`source`**.
- No element of **`destination`** is modified beyond the copied slice.
