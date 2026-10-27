<!-- Generated at publication from metadata.json — do not edit by hand -->

# 0018 — Squares

**Language:** C

**Difficulty:** 🟢 easy

**Tested skills:**
- for loop
- functions (pass by value)

## Task

Implement the two functions that compute the squares of the numbers up to a
given value:

1. **`ex_0018_Square`** receives an integer value and returns its square.
2. **`ex_0018_Squares`** receives an integer value that must be between 1
   and 1000, both included. If the value is out of range, the function
   prints nothing and returns **`false`**. Otherwise it prints the squares of
   the integers from 1 to the value, in increasing order, and returns
   **`true`**.

## Signature

- **`ex_0018_Square`** takes one parameter of type **`int`** and returns an
  **`int`**.
- **`ex_0018_Squares`** takes one parameter of type **`int`** and returns a
  **`bool`**.

## Expected output

A call to **`ex_0018_Squares(5)`** must print:

```
1 4 9 16 25 
```

## Constraints

- End the display of each square with a space.
- The output ends with a newline.
