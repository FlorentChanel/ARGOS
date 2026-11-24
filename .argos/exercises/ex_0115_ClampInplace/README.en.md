<!-- Generated at publication from metadata.json — do not edit by hand -->

# 0115 — Clamp Inplace

**Language:** C

**Difficulty:** 🟡 medium

**Tested skills:**
- pass by address

## Task

Implement **`ex_0115_ClampInplace`** so that it bounds the integer variable whose
address is passed as parameter to the interval [**`min`**, **`max`**]: a value
below **`min`** becomes **`min`**, a value above **`max`** becomes **`max`**, a
value inside the interval is left unchanged.

## Signature

**`ex_0115_ClampInplace`** takes three parameters: **`value`** of type pointer to
an **`int`**, then **`min`** and **`max`** of type **`int`**. It returns nothing.

## Examples

```c
int a = 15;
ex_0115_ClampInplace(&a, 0, 10);
```

**`a`** is now **`10`**.

```c
int b = -3;
ex_0115_ClampInplace(&b, 0, 10);
```

**`b`** is now **`0`**.

```c
int c = 7;
ex_0115_ClampInplace(&c, 0, 10);
```

**`c`** is still **`7`**.

```c
int d = -20;
ex_0115_ClampInplace(&d, -10, -5);
```

**`d`** is now **`-10`**.

## Constraints

- **`min`** is always less than or equal to **`max`**.
