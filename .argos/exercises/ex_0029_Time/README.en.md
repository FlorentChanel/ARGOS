<!-- Generated at publication from metadata.json — do not edit by hand -->

# 0029 — Time

**Language:** C

**Difficulty:** 🟡 medium

**Tested skills:**
- structures (struct)
- functions (pass by value)

## Task

Define, with a **`typedef`**, a **`Time`** structure that memorizes a
marathon time (hh:mm:ss). Then implement the three functions:

1. **`ex_0029_InitTime`** takes 3 integers (hours, minutes, seconds)
   passed as parameters and returns a **`Time`** structure.
2. **`ex_0029_PrintTime`** takes a **`Time`** structure as parameter and
   prints the associated time.
3. **`ex_0029_Time`** creates a **`Time`** structure holding 5 hours, 3
   minutes and 17 seconds using **`ex_0029_InitTime`** and prints it
   using **`ex_0029_PrintTime`**.

## Signature

**`Time`** is a structure type with three members: **`hh`** (hours),
**`mm`** (minutes) and **`ss`** (seconds).

- **`ex_0029_InitTime`** takes three **`int`** parameters, in this
  order: the hours, the minutes and the seconds. It returns a
  **`Time`**.
- **`ex_0029_PrintTime`** takes a **`Time`** parameter and returns
  nothing.
- **`ex_0029_Time`** takes no parameter and returns nothing.

## Expected output

```c
Time t = ex_0029_InitTime(5, 3, 17);
ex_0029_PrintTime(t);
```

prints **`05:03:17`**.

## Constraints

- The inputs are always valid: hours from 0 to 99, minutes and seconds
  from 0 to 59.
- The output ends with a newline.
