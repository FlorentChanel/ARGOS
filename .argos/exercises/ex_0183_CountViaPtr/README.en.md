<!-- Generated at publication from metadata.json — do not edit by hand -->

# 0183 — Count Via Ptr

**Language:** C

**Difficulty:** 🟢 easy

**Tested skills:**
- pointers / dereferencing

## Task

Implement **`ex_0183_CountViaPtr`** so that it counts the elements of an integer
array equal to a given value, and stores this count in the variable whose address
is passed as parameter.

## Signature

**`ex_0183_CountViaPtr`** takes four parameters: **`values`**, an array of
**`int`** (not modified), **`size`** of type **`int`**, the number of elements of
**`values`**, **`target`** of type **`int`**, the value to count, and **`count`**
of type pointer to an **`int`**. It returns nothing.

## Examples

```c
int data[] = {3, 1, 3, 7, 3};
int n;
ex_0183_CountViaPtr(data, 5, 3, &n);
```

**`n`** is now **`3`**.

```c
int data[] = {-2, 4, -2, 0};
int n;
ex_0183_CountViaPtr(data, 4, -2, &n);
```

**`n`** is now **`2`**.

```c
int data[] = {5, 6, 8};
int n = 42;
ex_0183_CountViaPtr(data, 3, 9, &n);
```

**`n`** is now **`0`**.

```c
int data[] = {1, 1, 1};
int n = 10;
ex_0183_CountViaPtr(data, 3, 1, &n);
```

**`n`** is now **`3`**.

```c
int data[] = {7};
int n = 5;
ex_0183_CountViaPtr(data, 0, 7, &n);
```

**`n`** is now **`0`**.
