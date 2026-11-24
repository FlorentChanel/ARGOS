<!-- Generated at publication from metadata.json — do not edit by hand -->

# 0184 — Deref Modify

**Language:** C

**Difficulty:** 🟡 medium

**Tested skills:**
- pointers / dereferencing

## Task

Implement **`ex_0184_DerefModify`** so that it adds **`delta`** to the integer
variable whose address is passed as parameter.

## Signature

**`ex_0184_DerefModify`** takes two parameters: **`value`** of type pointer to
an **`int`**, and **`delta`** of type **`int`**. It returns nothing.

## Examples

```c
int a = 10;
ex_0184_DerefModify(&a, 5);
```

**`a`** is now **`15`**.

```c
int b = 3;
ex_0184_DerefModify(&b, -8);
```

**`b`** is now **`-5`**.

```c
int c = -4;
ex_0184_DerefModify(&c, 0);
```

**`c`** is still **`-4`**.

```c
int d = 1;
ex_0184_DerefModify(&d, 2);
ex_0184_DerefModify(&d, 2);
```

**`d`** is now **`5`**.
