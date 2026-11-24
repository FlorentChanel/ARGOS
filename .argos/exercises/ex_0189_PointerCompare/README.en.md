<!-- Generated at publication from metadata.json — do not edit by hand -->

# 0189 — Pointer Compare

**Language:** C

**Difficulty:** 🟡 medium

**Tested skills:**
- pointers / dereferencing

## Task

Implement **`ex_0189_PointerCompare`** so that it compares, element by element,
two zones of integers whose addresses are passed as parameters.

## Signature

**`ex_0189_PointerCompare`** takes three parameters: **`first`** and
**`second`**, two pointers to the first element of a zone of **`int`** (not
modified), and **`size`** of type **`int`**, the number of elements to compare.
It returns an **`int`**:

- **`0`** if the **`size`** elements of both zones are equal;
- **`-1`** if, at the first position where they differ, the element of
  **`first`** is smaller than the element of **`second`**;
- **`1`** if, at that position, the element of **`first`** is greater.

## Examples

```c
int a[] = {1, 2, 3, 4};
int b[] = {1, 2, 3, 4};
int result = ex_0189_PointerCompare(a, b, 4);
```

**`result`** is **`0`**.

```c
int a[] = {1, 2, 3, 4};
int b[] = {1, 2, 5, 0};
int result = ex_0189_PointerCompare(a, b, 4);
```

**`result`** is **`-1`**.

```c
int a[] = {7, -2, 9};
int b[] = {7, -8, 100};
int result = ex_0189_PointerCompare(a, b, 3);
```

**`result`** is **`1`**.

```c
int a[] = {5, 6, 7};
int b[] = {5, 6, 8};
int result = ex_0189_PointerCompare(a, b, 2);
```

**`result`** is **`0`**.

```c
int data[] = {3, 4, 3, 4, 9};
int result = ex_0189_PointerCompare(data, data + 2, 3);
```

**`result`** is **`-1`**.

```c
int a[] = {1};
int b[] = {2};
int result = ex_0189_PointerCompare(a, b, 0);
```

**`result`** is **`0`**.
