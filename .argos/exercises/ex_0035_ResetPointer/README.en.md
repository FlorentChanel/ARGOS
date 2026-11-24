<!-- Generated at publication from metadata.json — do not edit by hand -->

# 0035 — Reset Pointer

**Language:** C

**Difficulty:** 🟡 medium

**Tested skills:**
- pointers / dereferencing

## Task

Implement **`ex_0035_ResetPointer`** so that it sets to **`NULL`** the
pointer to **`int`** whose address is passed as parameter.

## Signature

**`ex_0035_ResetPointer`** takes one parameter **`pointer`** of type
pointer to a pointer to an **`int`**. It returns nothing.

## Examples

```c
int x = 42;
int *p = &x;
ex_0035_ResetPointer(&p);
```

**`p`** is now **`NULL`**, **`x`** is still **`42`**.

```c
int values[3] = {1, 2, 3};
int *q = &values[2];
ex_0035_ResetPointer(&q);
```

**`q`** is now **`NULL`**, **`values`** is still **`{1, 2, 3}`**.

```c
int *r = NULL;
ex_0035_ResetPointer(&r);
```

**`r`** is still **`NULL`**.
