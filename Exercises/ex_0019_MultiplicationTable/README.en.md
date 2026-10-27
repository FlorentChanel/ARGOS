<!-- Generated at publication from metadata.json — do not edit by hand -->

# 0019 — Multiplication Table

**Language:** C

**Difficulty:** 🟢 easy

**Tested skills:**
- for loop
- functions (pass by value)

## Task

Implement the two functions that input a number between two values and
print its multiplication table:

1. **`ex_0019_Read`** receives 2 integer parameters: a min value and a max
   value between which the number entered on the keyboard must lie, min
   and max bounds included. Its prompt displays these two values in the
   **`[min..max]`** part. It returns the entered number.
2. **`ex_0019_MultiplicationTable`** prints the requested multiplication
   table, from 1 to 10, as in the examples below.

The provided **`main()`** only consists of two calls to these functions.

## Signature

- **`ex_0019_Read`** takes two parameters of type **`int`** (the min and
  max values) and returns an **`int`**.
- **`ex_0019_MultiplicationTable`** takes one parameter of type **`int`**
  and returns nothing (**`void`**).

## Expected output

```
Please enter the multiplication table (in [1..12]): 0
Please enter the multiplication table (in [1..12]): 13
Please enter the multiplication table (in [1..12]): a
Please enter the multiplication table (in [1..12]): 5

MULTIPLICATION TABLE FOR 5
5 X 1 = 5
5 X 2 = 10
5 X 3 = 15
5 X 4 = 20
5 X 5 = 25
5 X 6 = 30
5 X 7 = 35
5 X 8 = 40
5 X 9 = 45
5 X 10 = 50
```

On its own, a call to **`ex_0019_MultiplicationTable(5)`** must print the
following, starting with the empty line:

```

MULTIPLICATION TABLE FOR 5
5 X 1 = 5
5 X 2 = 10
5 X 3 = 15
5 X 4 = 20
5 X 5 = 25
5 X 6 = 30
5 X 7 = 35
5 X 8 = 40
5 X 9 = 45
5 X 10 = 50
```

## Constraints

- After each **`scanf`**, flush **`stdin`**: discard the rest of the line, up to
  **`\n`** or **`EOF`** (see [Reading from stdin](https://github.com/HE-Arc/ARGOS#reading-from-stdin)).
- **`ex_0019_MultiplicationTable`** only receives a table number between 1
  and 12, bounds included.
- The output ends with a newline.
