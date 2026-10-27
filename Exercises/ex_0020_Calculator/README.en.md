<!-- Generated at publication from metadata.json — do not edit by hand -->

# 0020 — Calculator

**Language:** C

**Difficulty:** 🟡 medium

**Tested skills:**
- conditionals (if / switch)
- functions (pass by value)

## Task

Implement **`ex_0020_Calculator`** so that it performs simple mathematical
operations: **`+`**, **`-`**, **`*`**, **`/`**. The function returns the result of the operation
indicated by the operator, applied to its two operands.

Take the risk of a division by zero into account: in that case, the
function returns zero. The function also returns zero when the character
is not one of the four operators.

## Signature

**`ex_0020_Calculator`** takes three parameters, in this order: two
**`double`** operands and a **`char`** operator. It returns a **`double`**.

## Examples

| Call                                    | returned value |
|-----------------------------------------|----------------|
| **`ex_0020_Calculator(1, 2, '+')`**     | 3              |
| **`ex_0020_Calculator(1, 2, '-')`**     | -1             |
| **`ex_0020_Calculator(1.1, 9.9, '*')`** | 10.89          |
| **`ex_0020_Calculator(1, 2, '/')`**     | 0.5            |
| **`ex_0020_Calculator(1, 0, '/')`**     | 0              |
| **`ex_0020_Calculator(1, 2, 'z')`**     | 0              |
