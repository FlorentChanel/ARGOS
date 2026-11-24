<!-- Generated at publication from metadata.json — do not edit by hand -->

# 0185 — Array Sum Ptr

**Language:** C

**Difficulty:** 🟡 medium

**Tested skills:**
- pointers / dereferencing

## Task

Implement **`ex_0185_ArraySumPtr`** so that it returns the sum of the elements of
an integer array whose address is passed as parameter.

## Signature

**`ex_0185_ArraySumPtr`** takes two parameters: **`values`**, a pointer to the
first element of an array of **`int`** (not modified), and **`size`** of type
**`int`**, the number of elements of the array. It returns the sum of the
elements as an **`int`**.

## Examples

```c
int data[] = {1, 2, 3, 4};
int sum = ex_0185_ArraySumPtr(data, 4);
```

**`sum`** is **`10`**.

```c
int data[] = {-5, 8, -3, 2, 7};
int sum = ex_0185_ArraySumPtr(data, 5);
```

**`sum`** is **`9`**.

```c
int data[] = {42};
int sum = ex_0185_ArraySumPtr(data, 1);
```

**`sum`** is **`42`**.

```c
int data[] = {10, 20, 30, 40};
int sum = ex_0185_ArraySumPtr(data + 1, 2);
```

**`sum`** is **`50`**.

```c
int data[] = {7};
int sum = ex_0185_ArraySumPtr(data, 0);
```

**`sum`** is **`0`**.

## Constraints

- **`size`** is at least 0 and **`values`** has at least **`size`** elements.
- Every partial sum and the sum fit in an **`int`**.
