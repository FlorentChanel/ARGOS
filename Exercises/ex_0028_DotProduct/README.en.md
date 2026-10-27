<!-- Generated at publication from metadata.json — do not edit by hand -->

# 0028 — Dot Product

**Language:** C

**Difficulty:** 🟢 easy

**Tested skills:**
- 1D arrays

## Task

Implement **`ex_0028_DotProduct`** so that it computes the dot product of 2
integer vectors $\vec{u}$ and $\vec{v}$. The vectors are passed as
parameters as integer arrays, with their size, in this order.

The dot product is the sum of the products of the elements with the same
index, for the **`n`** elements:

$$\vec{u} \cdot \vec{v} = u_0 v_0 + u_1 v_1 + \dots + u_{n-1} v_{n-1}$$

## Signature

**`ex_0028_DotProduct`** takes two integer arrays (**`int`**), then their size
**`n`** (**`int`**), in this order, and returns their dot product (**`int`**).

## Examples

With the following arrays:

```c
int u[] = {3, 2, -4};
int v[] = {2, -3, 5};
```

**`ex_0028_DotProduct(u, v, 3)`** returns **`-20`**
($3 \times 2 + 2 \times (-3) + (-4) \times 5 = -20$).

## Constraints

- **`n`** is at least 1 and both arrays have **`n`** elements.
- Every product $u_i v_i$, every partial sum and the dot product fit in an
  **`int`**.
