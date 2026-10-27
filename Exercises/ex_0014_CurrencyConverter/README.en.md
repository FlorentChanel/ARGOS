<!-- Generated at publication from metadata.json — do not edit by hand -->

# 0014 — Currency Converter

**Language:** C

**Difficulty:** 🟡 medium

**Tested skills:**
- conditionals (if / switch)

## Task

Complete **`ex_0014_CurrencyConverter`** so that it converts to Swiss
francs an amount given in won (W), dollars ($), yen (Y) or pounds
sterling (P). For the input, use one of the following instructions:

```c
scanf(" %g %c", &amount, &currency); // To store in a float
```

or

```c
scanf(" %lg %c", &amount, &currency); // To store in a double
```

For the exchange rates, use the following constants:

```c
const double WON2CHF = 0.00070;
const double USD2CHF = 0.99;
const double YEN2CHF = 0.0067;
const double POUND2CHF = 1.13;
```

## Signature

```c
void ex_0014_CurrencyConverter(void);
```

## Examples

```
USAGE: non-negative value [W | $ | Y | P]
Won = W  Dollar = $  Yen = Y  Pound = P
Please enter the amount to convert: 123 W
Swiss francs: 0.086
```

```
USAGE: non-negative value [W | $ | Y | P]
Won = W  Dollar = $  Yen = Y  Pound = P
Please enter the amount to convert: 123 $
Swiss francs: 121.770
```

```
USAGE: non-negative value [W | $ | Y | P]
Won = W  Dollar = $  Yen = Y  Pound = P
Please enter the amount to convert: -123 Y
The input amount is negative!!
USAGE: non-negative value [W | $ | Y | P]
Won = W  Dollar = $  Yen = Y  Pound = P
Please enter the amount to convert: 123 Y
Swiss francs: 0.824
```

```
USAGE: non-negative value [W | $ | Y | P]
Won = W  Dollar = $  Yen = Y  Pound = P
Please enter the amount to convert: 123 L
Unsupported currency!!
USAGE: non-negative value [W | $ | Y | P]
Won = W  Dollar = $  Yen = Y  Pound = P
Please enter the amount to convert: 123 P
Swiss francs: 138.990
```

```
USAGE: non-negative value [W | $ | Y | P]
Won = W  Dollar = $  Yen = Y  Pound = P
Please enter the amount to convert: d W
The input format is not correct!!
USAGE: non-negative value [W | $ | Y | P]
Won = W  Dollar = $  Yen = Y  Pound = P
Please enter the amount to convert: 122 W
Swiss francs: 0.085
```

## Constraints

- Print the reals with 3 digits after the decimal point.
- Handle input errors (wrong format, unsupported currency, negative
  amount): print the matching provided message and prompt again.
- If the input format is wrong, print only **`The input format is not correct!!`**.
  Otherwise, check the currency first, then the amount: if both are invalid,
  print **`Unsupported currency!!`** then **`The input amount is negative!!`**.
- Only the uppercase letters **`W`**, **`Y`** and **`P`** are supported:
  lowercase letters (**`w`**, **`y`**, **`p`**) are unsupported currencies.
- After each **`scanf`**, flush **`stdin`**: discard the rest of the line, up to
  **`\n`** or **`EOF`** (see [Reading from stdin](https://github.com/HE-Arc/ARGOS#reading-from-stdin)).
- The output ends with a newline.
