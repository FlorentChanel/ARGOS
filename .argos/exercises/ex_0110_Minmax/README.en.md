<!-- Generated at publication from metadata.json — do not edit by hand -->

# 0110 — Minmax

**Language:** C

**Difficulty:** 🟢 easy

**Tested skills:**
- pass by address

## Task

Implement **`ex_0110_Minmax`** so that it stores the smallest and the largest of
three integers in the two variables whose addresses are passed as parameters.

## Signature

**`ex_0110_Minmax`** takes five parameters: **`a`**, **`b`** and **`c`** of type
**`int`**, then **`min`** and **`max`**, each of type pointer to an **`int`**.
It returns nothing.

## Examples

```c
int lo;
int hi;
ex_0110_Minmax(4, 9, 2, &lo, &hi);
```

**`lo`** is now **`2`** and **`hi`** is now **`9`**.

```c
int lo;
int hi;
ex_0110_Minmax(-3, 0, -8, &lo, &hi);
```

**`lo`** is now **`-8`** and **`hi`** is now **`0`**.

```c
int lo;
int hi;
ex_0110_Minmax(5, 5, 1, &lo, &hi);
```

**`lo`** is now **`1`** and **`hi`** is now **`5`**.

```c
int lo;
int hi;
ex_0110_Minmax(7, 7, 7, &lo, &hi);
```

**`lo`** and **`hi`** are now both **`7`**.
