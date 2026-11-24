<!-- Generated at publication from metadata.json — do not edit by hand -->

# 0182 — String Via Ptr

**Language:** C

**Difficulty:** 🟢 easy

**Tested skills:**
- pointers / dereferencing

## Task

Implement **`ex_0182_StringViaPtr`** so that it returns the number of characters
of the string passed as parameter, by walking through it with a pointer.

## Signature

**`ex_0182_StringViaPtr`** takes one parameter: **`text`** of type pointer to a
constant **`char`** (a null-terminated string). It returns an **`int`**: the
number of characters of **`text`**, the terminating **`'\0'`** not included.

## Examples

```c
ex_0182_StringViaPtr("hello")
```

returns **`5`**.

```c
ex_0182_StringViaPtr("")
```

returns **`0`**.

```c
ex_0182_StringViaPtr("a b c")
```

returns **`5`**.

```c
ex_0182_StringViaPtr("C\n")
```

returns **`2`**.

## Constraints

- Do not use **`strlen`** or any other function of **`string.h`**.
- Do not use the **`[]`** operator.
