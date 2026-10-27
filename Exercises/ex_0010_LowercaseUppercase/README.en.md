<!-- Generated at publication from metadata.json — do not edit by hand -->

# 0010 — Lowercase Uppercase

**Language:** C

**Difficulty:** 🟡 medium

**Tested skills:**
- conditionals (if / switch)

## Task

Complete **`ex_0010_LowercaseUppercase`** so that it determines whether the
typed character is a lowercase letter (ASCII code between 97 and 122) or an
uppercase letter (code between 65 and 90).

## Signature

```c
void ex_0010_LowercaseUppercase(void);
```

## Examples

```
Type a letter: u
lowercase
```

```
Type a letter: F
UPPERCASE
```

```
Type a letter: !
The character you entered is not a letter.
```

## Constraints

- Handle input errors: keep prompting until a character is read.
- After each **`scanf`**, flush **`stdin`**: discard the rest of the line, up to
  **`\n`** or **`EOF`** (see [Reading from stdin](https://github.com/HE-Arc/ARGOS#reading-from-stdin)).
- The output ends with a newline.
