<!-- Generated at publication from metadata.json — do not edit by hand -->

# 0013 — Second Order Equation

**Language:** C

**Difficulty:** 🟡 medium

**Tested skills:**
- conditionals (if / switch)

## Task

Complete **`ex_0013_SecondOrderEquation`** so that it computes the real
solution(s) of a quadratic equation of the form

$$ax^2 + bx + c = 0$$

using the formula

$$x_{1,2} = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$$

Also consider the cases where the user enters:

- a zero value for **`a`**;
- zero values for **`a`** and **`b`**;
- zero values for **`a`**, **`b`** and **`c`**.

Print the necessary results and messages on the screen (the messages are
provided in the skeleton).

## Signature

```c
void ex_0013_SecondOrderEquation(void);
```

## Examples

```
Compute solutions of an equation of the form ax^2 + bx + c = 0
Please enter coefficients a, b, and c: 0 0 0
Any real is solution of this equation.
```

```
Compute solutions of an equation of the form ax^2 + bx + c = 0
Please enter coefficients a, b, and c: 1 1 1
This equation has no real solution.
```

```
Compute solutions of an equation of the form ax^2 + bx + c = 0
Please enter coefficients a, b, and c: 1 1 -2
The real solutions of this equation are: 
x1 = 1.0000
x2 = -2.0000
```

```
Compute solutions of an equation of the form ax^2 + bx + c = 0
Please enter coefficients a, b, and c: 1 -2 1
The double real solution of this equation is: 
x = 1.0000
```

```
Compute solutions of an equation of the form ax^2 + bx + c = 0
Please enter coefficients a, b, and c: 0 2 -4
The solution of this linear equation is: 
x = 2.0000
```

```
Compute solutions of an equation of the form ax^2 + bx + c = 0
Please enter coefficients a, b, and c: 0 0 5
This equation has no solution.
```

```
Compute solutions of an equation of the form ax^2 + bx + c = 0
Please enter coefficients a, b, and c: a 1 2
Compute solutions of an equation of the form ax^2 + bx + c = 0
Please enter coefficients a, b, and c: 1 b -2
Compute solutions of an equation of the form ax^2 + bx + c = 0
Please enter coefficients a, b, and c: 2 -1 -2
The real solutions of this equation are: 
x1 = 1.2808
x2 = -0.7808
```

## Constraints

- The coefficients **`a`**, **`b`** and **`c`** are real numbers: decimal
  input such as **`0.5`** is accepted.
- Print the reals with 4 digits after the decimal point.
- A zero solution may be printed as **`0.0000`** or **`-0.0000`**: both are
  accepted.
- Handle input errors: keep prompting until three numbers are read.
- After each **`scanf`**, flush **`stdin`**: discard the rest of the line, up to
  **`\n`** or **`EOF`** (see [Reading from stdin](https://github.com/HE-Arc/ARGOS#reading-from-stdin)).
- The output ends with a newline.
