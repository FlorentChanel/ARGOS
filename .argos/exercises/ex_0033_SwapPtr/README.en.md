<!-- Generated at publication from metadata.json — do not edit by hand -->

# 0033 — Swap Ptr

**Language:** C

**Difficulty:** 🟢 easy

**Tested skills:**
- pass by address

## Task

Implement **`ex_0033_SwapPtr`** so that it swaps the values of the two
integer variables whose addresses are passed as parameters.

## Signature

**`ex_0033_SwapPtr`** takes two parameters **`a`** and **`b`**, each of type
pointer to an **`int`**. It returns nothing.

## Examples

```c
int x = 3;
int y = 8;
ex_0033_SwapPtr(&x, &y);
```

**`x`** is now **`8`** and **`y`** is now **`3`**.

```c
int x = -5;
int y = 0;
ex_0033_SwapPtr(&x, &y);
```

**`x`** is now **`0`** and **`y`** is now **`-5`**.

```c
int x = 7;
int y = 7;
ex_0033_SwapPtr(&x, &y);
```

**`x`** and **`y`** are still **`7`**.
