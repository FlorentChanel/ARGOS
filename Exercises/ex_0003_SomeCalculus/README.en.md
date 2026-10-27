<!-- Generated at publication from metadata.json — do not edit by hand -->

# 0003 — Some Calculus

**Language:** C

**Difficulty:** 🟢 easy

**Tested skills:**
- arithmetic operators
- variables and types

## Task

Complete **`ex_0003_SomeCalculus`** so that it computes the following five values
from the two real numbers **`a`** and **`b`**:

1. $a^b$ (**`a`** raised to the power **`b`**)
2. the hypotenuse of a right triangle whose legs are **`a`** and **`b`**: $\sqrt{a^2 + b^2}$
3. the tangent of **`a`**, where **`a`** is an angle **in degrees**
4. $a / b$ rounded down to an integer
5. $a / b$ rounded down to 3 decimal places

The **`printf`** calls are already provided in the skeleton: for each step, only
compute the value and store it in **`res`**.

## Signature

```c
void ex_0003_SomeCalculus(double a, double b);
```

## Expected output

For **`a = 4`** and **`b = 7`**, the function prints:

```
 a) 4.000000 power 7.000000 = 16384 

 b) The hypotenuse of the right triangle is 8.062258 

 c) The tangent of A is 0.069927 

 d) The rounded down value of A/B is 0.000000 

 e) The rounded down value of A/B with 3 decimals is 0.571000 
```

The output starts with an empty line (before part a)) and ends with an empty line
(after part e)).

## Constraints

- The inputs are always valid: **`b`** is non-zero, $a^b$ is defined (**`a`** is
  not negative when **`b`** is not an integer), and **`a`** is not an odd multiple
  of 90 degrees.
- Use the functions of the standard math library (**`math.h`** is already
  included): **`pow`**, **`sqrt`**, **`sin`**, **`cos`**, **`floor`**.
- Compute the tangent using only **`sin`** and **`cos`**.
- Do not modify the provided **`printf`** calls or the function signature.

> [!WARNING]
> The trigonometric functions of **`math.h`** work in **radians**, while **`a`** is
> given in **degrees**.
