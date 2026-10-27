<!-- Generated at publication from metadata.json — do not edit by hand -->

# 0009 — Circle

**Language:** C

**Difficulty:** 🟡 medium

**Tested skills:**
- formatted input/output

## Task

Complete **`ex_0009_Circle`** so that it computes the surface of a circle
when the user enters the radius. The radius is a real number
(**`double`**); the input is always a valid non-negative value.

Before the surface, the function prints pi (the provided **`M_PI`**) with
6 digits after the decimal point. The surface is printed with 2 digits
after the decimal point.

## Signature

```c
void ex_0009_Circle(void);
```

## Expected output

The console session looks like this (**`1`** is typed by the user):

```
Circle radius: 1
pi = 3.141593
Circle surface = 3.14
```

> [!WARNING]
> The output ends with a newline.

## Constraints

- After each **`scanf`**, flush **`stdin`**: discard the rest of the line, up to
  **`\n`** or **`EOF`** (see [Reading from stdin](https://github.com/HE-Arc/ARGOS#reading-from-stdin)).
