<!-- Generated at publication from metadata.json — do not edit by hand -->

# 0015 — Days In Month

**Language:** C

**Difficulty:** 🟡 medium

**Tested skills:**
- conditionals (if / switch)

## Task

Complete **`ex_0015_DaysInMonth`** so that it asks the user for a month
number (1 for January, 2 for February, ...) and prints the corresponding
number of days (31 days in January, 28 in February, ...).

The result line is **`Month <n> has <d> days.`**, where **`<n>`** is the month
number and **`<d>`** its number of days.

## Signature

```c
void ex_0015_DaysInMonth(void);
```

## Examples

```
Please enter the number of the month (january=1, ... , december=12): 1
Month 1 has 31 days.
```

```
Please enter the number of the month (january=1, ... , december=12): 12
Month 12 has 31 days.
```

```
Please enter the number of the month (january=1, ... , december=12): 13
Please enter the number of the month (january=1, ... , december=12): 7
Month 7 has 31 days.
```

```
Please enter the number of the month (january=1, ... , december=12): a
Please enter the number of the month (january=1, ... , december=12): b
Please enter the number of the month (january=1, ... , december=12): 0
Please enter the number of the month (january=1, ... , december=12): 8
Month 8 has 31 days.
```

## Constraints

- Use a **`switch`** on the month to find its number of days.
- Handle input errors: keep prompting until a month between 1 and 12 is read.
- After each **`scanf`**, flush **`stdin`**: discard the rest of the line, up to
  **`\n`** or **`EOF`** (see [Reading from stdin](https://github.com/HE-Arc/ARGOS#reading-from-stdin)).
- The output ends with a newline.
