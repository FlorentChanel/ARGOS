<!-- Generated at publication from metadata.json — do not edit by hand -->

# 0016 — Sum Product Mean

**Language:** C

**Difficulty:** 🔴 hard

**Tested skills:**
- for loop
- formatted input/output

## Task

Complete **`ex_0016_SumProductMean`** so that it:

1. reads **`N`** integers from the keyboard and prints their sum, their
   product and their mean — choose an appropriate type for the values to
   print, and use the most appropriate loop;
2. repeats the input of the number **`N`** until **`N`** has a value
   between 1 and 15.

## Signature

```c
void ex_0016_SumProductMean(void);
```

## Expected output

The console session looks like this (the text after each prompt, **`16`**, **`0`**,
**`-1`**, **`3`**, **`a`**, **`1`**, **`b`**, **`2`**, **`c`** and **`3`**, is typed by the user):

```
Number of values to read: 16
Number of values to read: 0
Number of values to read: -1
Number of values to read: 3
1. number: a
1. number: 1
2. number: b
2. number: 2
3. number: c
3. number: 3
Sum = 6
Product = 6
Mean = 2.0000
```

## Constraints

- The tests use integers between -4 and 4: the sum and the product always fit in an
  **`int`** and are printed as integers.
- Print the reals with 4 digits after the decimal point.
- Handle input errors: keep prompting until a valid number is read.
- After each **`scanf`**, flush **`stdin`**: discard the rest of the line, up to
  **`\n`** or **`EOF`** (see [Reading from stdin](https://github.com/HE-Arc/ARGOS#reading-from-stdin)).
- The output ends with a newline.
