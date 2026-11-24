<!-- Generated at publication from metadata.json — do not edit by hand -->

# 0111 — Div Mod

**Language:** C

**Difficulty:** 🟡 medium

**Tested skills:**
- pass by address

## Task

Implement **`ex_0111_DivMod`** so that it computes the integer quotient and the
remainder of the division of **`dividend`** by **`divisor`**, and stores them in
the two integer variables whose addresses are passed as parameters.

## Signature

**`ex_0111_DivMod`** takes four parameters: **`dividend`** and **`divisor`** of
type **`int`**, then **`quotient`** and **`remainder`** of type pointer to an
**`int`**. It returns nothing.

## Examples

```c
int q = 0;
int r = 0;
ex_0111_DivMod(17, 5, &q, &r);
```

**`q`** is now **`3`** and **`r`** is now **`2`**.

```c
int q = 0;
int r = 0;
ex_0111_DivMod(20, 4, &q, &r);
```

**`q`** is now **`5`** and **`r`** is now **`0`**.

```c
int q = 0;
int r = 0;
ex_0111_DivMod(3, 8, &q, &r);
```

**`q`** is now **`0`** and **`r`** is now **`3`**.

```c
int q = 0;
int r = 0;
ex_0111_DivMod(-17, 5, &q, &r);
```

**`q`** is now **`-3`** and **`r`** is now **`-2`**.

## Constraints

- **`divisor`** is never **`0`**.
- The quotient always fits in an **`int`**: **`dividend`** is never
  **`INT_MIN`** when **`divisor`** is **`-1`**.
