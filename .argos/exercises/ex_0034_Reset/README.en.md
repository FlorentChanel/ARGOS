<!-- Generated at publication from metadata.json — do not edit by hand -->

# 0034 — Reset

**Language:** C

**Difficulty:** 🟢 easy

**Tested skills:**
- pointers / dereferencing

## Task

Implement **`ex_0034_Reset`** so that it sets to zero the integer variable
whose address is passed as parameter.

## Signature

**`ex_0034_Reset`** takes one parameter **`value`** of type pointer to
an **`int`**. It returns nothing.

## Examples

```c
int a = 42;
ex_0034_Reset(&a);
```

**`a`** is now **`0`**.

```c
int b = -7;
ex_0034_Reset(&b);
```

**`b`** is now **`0`**.

```c
int c = 0;
ex_0034_Reset(&c);
```

**`c`** is still **`0`**.
