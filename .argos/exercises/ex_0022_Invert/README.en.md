<!-- Generated at publication from metadata.json — do not edit by hand -->

# 0022 — Invert

**Language:** C

**Difficulty:** 🟡 medium

**Tested skills:**
- while loop
- functions (pass by value)

## Task

Implement **`ex_0022_Invert`** so that it inverts the digits composing an
integer number. Any negative input is an error: the function then returns
**`-1`**.

## Signature

**`ex_0022_Invert`** takes one parameter: the **`int`** number **`n`** to
invert. It returns an **`int`**.

## Examples

| Call                         | returned value |
|------------------------------|----------------|
| **`ex_0022_Invert(1234)`**   | 4321           |
| **`ex_0022_Invert(1200)`**   | 21             |
| **`ex_0022_Invert(0)`**      | 0              |
| **`ex_0022_Invert(-12)`**    | -1             |

## Constraints

- When **`n`** is not negative, its inverted value fits in an **`int`**
  (inputs such as **`1000000009`** are excluded).
