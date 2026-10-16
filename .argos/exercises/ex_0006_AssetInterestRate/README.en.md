<!-- Generated at publication from metadata.json — do not edit by hand -->

# 0006 — Asset Interest Rate

**Language:** C

**Difficulty:** 🟡 medium

**Tested skills:**
- arithmetic operators
- variables and types

## Task

Complete **`ex_0006_AssetInterestRate`** so that it computes the final value
of an asset with initial value **`initAssets`**, after applying a yearly
compound interest rate of **`interestRate`** (in percent) for
**`years`** years, and returns it:

$$\text{finalAssets} = \text{initAssets} \times \left(1 + \frac{\text{interestRate}}{100}\right)^{\text{years}}$$

## Signature

```c
double ex_0006_AssetInterestRate(double initAssets, double interestRate, int years);
```

## Examples

| **`initAssets`** | **`interestRate`** | **`years`**    | returned value |
|------------------|--------------------|----------------|----------------|
| 1000             | 2.5                | 30             | ≈ 2097.57      |
| 1000             | 2.5                | 0              | 1000           |
| 1000             | 0                  | 30             | 1000           |
| 1000             | 2.5                | 1              | 1025           |

## Constraints

- Use **`pow`** from the standard math library (**`math.h`** is already
  included).
- The inputs are always valid: **`years`** is non-negative and
  **`interestRate`** is greater than -100.
