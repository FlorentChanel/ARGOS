<!-- Generated at publication from metadata.json — do not edit by hand -->

# 0030 — Complex

**Language:** C

**Difficulty:** 🔴 hard

**Tested skills:**
- structures (struct)
- functions (pass by value)

## Task

Implement the type and the functions that manage complex numbers:

1. Define the **`Complex`** type with 2 members of type **`double`**:
   **`real`** and **`imaginary`**.
2. **`ex_0030_InputComplex`** reads a complex number, only accepting the
   **`(r,i)`** format, and returns a **`Complex`** structure. Before each
   read attempt, it prints the prompt shown in the example below.
3. **`ex_0030_SumComplex`** and **`ex_0030_DiffComplex`** compute the sum
   and the difference of two complex numbers stored in a **`Complex`**
   structure.

   $(a_1 + i b_1) + (a_2 + i b_2) = (a_1+a_2) + i(b_1+b_2)$

   $(a_1 + i b_1) - (a_2 + i b_2) = (a_1-a_2) + i(b_1-b_2)$

4. **`ex_0030_PrintComplex`** prints a complex number in the following
   form, followed by a newline: **`5.00 + -3.00i`**.
5. **`ex_0030_Complex`** reads two complex numbers, computes their sum
   and their difference and prints the results, using the functions
   written in the previous points.

## Signature

- **`ex_0030_InputComplex`** takes no parameter and returns a
  **`Complex`**.
- **`ex_0030_SumComplex`** and **`ex_0030_DiffComplex`** each take two
  parameters of type **`Complex`** and return a **`Complex`**.
- **`ex_0030_PrintComplex`** takes one parameter of type **`Complex`**
  and returns nothing (**`void`**).
- **`ex_0030_Complex`** takes no parameter and returns nothing
  (**`void`**).

## Expected output

```
Please enter a complex number (r,i): a
Please enter a complex number (r,i): -1
Please enter a complex number (r,i): (1, 1)
Please enter a complex number (r,i): (2, 3)

Sum = 3.00 + 4.00i

Diff = -1.00 + -2.00i
```

On its own, a call to **`ex_0030_PrintComplex`** with a real part of
**`5`** and an imaginary part of **`-3`** prints the following line,
followed by a newline:

```
5.00 + -3.00i
```

## Constraints

- Handle input errors: keep prompting until the **`(r,i)`** format is read.
- Spaces and tabs are accepted around the numbers and around the parentheses; any
  other character outside the **`(r,i)`** format makes the input invalid.
- After each **`scanf`**, flush **`stdin`**: discard the rest of the line, up to
  **`\n`** or **`EOF`** (see [Reading from stdin](https://github.com/HE-Arc/ARGOS#reading-from-stdin)).
