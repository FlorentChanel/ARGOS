<!-- Generated at publication from metadata.json — do not edit by hand -->

# 0008 — Scanf Printf

**Language:** C

**Difficulty:** 🟢 easy

**Tested skills:**
- formatted input/output

## Task

Complete **`ex_0008_ScanfPrintf`** so that it asks the user for 3 letters
and prints their ASCII codes. The input always holds 3 letters; they may be
typed with no separator (**`abc`**), separated by spaces (**`a b c`**) or
separated by newlines.

## Signature

```c
void ex_0008_ScanfPrintf(void);
```

## Expected output

The console session looks like this (**`a b c`** is typed by the user):

```


Please enter 3 letters:
a b c

Here are the corresponding ASCII codes:
a--------->97
b--------->98
c--------->99
```

The function prints exactly:

1. **`"\n\nPlease enter 3 letters:\n"`** before reading the letters (two
   newlines, then the prompt, which ends with a newline);
2. **`"\nHere are the corresponding ASCII codes:\n"`** after reading them:
   the empty line above this line is printed by the function, not echoed
   by the user's Enter;
3. one line per letter, in the order typed: the letter, **`--------->`**,
   then its ASCII code, followed by a newline.

> [!WARNING]
> The output starts with two newlines and ends with a newline.

## Constraints

> [!WARNING]
> After reading the third letter (with **`scanf`**), you **must** flush
> **`stdin`** (up to **`\n`** or **`EOF`**).
> See [Reading from stdin](https://github.com/HE-Arc/ARGOS#reading-from-stdin).
