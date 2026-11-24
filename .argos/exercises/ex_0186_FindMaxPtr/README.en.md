<!-- Generated at publication from metadata.json — do not edit by hand -->

# 0186 — Find Max Ptr

**Language:** C

**Difficulty:** 🟡 medium

**Tested skills:**
- pointers / dereferencing

## Task

Implement **`ex_0186_FindMaxPtr`** so that it returns the address of the
largest element of an array of integers. When the largest value appears several
times, it returns the address of its first occurrence.

## Signature

**`ex_0186_FindMaxPtr`** takes two parameters: **`values`** of type pointer to
an **`int`** (the first element of the array), and **`size`** of type **`int`**
(the number of elements). It returns a pointer to an **`int`**.

## Examples

```c
int values[] = {3, 8, 1, 6};
int *p = ex_0186_FindMaxPtr(values, 4);
```

**`p`** is **`&values[1]`** and **`*p`** is **`8`**.

```c
int values[] = {-7, -2, -9};
int *p = ex_0186_FindMaxPtr(values, 3);
```

**`p`** is **`&values[1]`** and **`*p`** is **`-2`**.

```c
int values[] = {5, 9, 2, 9};
int *p = ex_0186_FindMaxPtr(values, 4);
```

**`p`** is **`&values[1]`** and **`*p`** is **`9`**.

```c
int values[] = {4};
int *p = ex_0186_FindMaxPtr(values, 1);
```

**`p`** is **`&values[0]`** and **`*p`** is **`4`**.

```c
int values[] = {2, 7, 4};
*ex_0186_FindMaxPtr(values, 3) = 0;
```

**`values`** is now **`{2, 0, 4}`**.

## Constraints

- **`size`** is at least **`1`**.
