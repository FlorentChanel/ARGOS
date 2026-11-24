<!-- Generated at publication from metadata.json — do not edit by hand -->

# 0114 — Accumulate Stats

**Language:** C

**Difficulty:** 🟡 medium

**Tested skills:**
- pass by address

## Task

Implement **`ex_0114_AccumulateStats`** so that it computes the sum and the mean
of the first **`count`** integers of the array **`values`**, and stores them in
the two variables whose addresses are passed as parameters.

## Signature

**`ex_0114_AccumulateStats`** takes four parameters: **`values`**, an array of
**`int`** that it does not modify, **`count`** of type **`int`**, then **`sum`**
of type pointer to an **`int`** and **`mean`** of type pointer to a
**`double`**. It returns nothing.

## Examples

```c
int values[] = {1, 2, 3, 4};
int sum;
double mean;
ex_0114_AccumulateStats(values, 4, &sum, &mean);
```

**`sum`** is now **`10`** and **`mean`** is now **`2.5`**.

```c
int values[] = {-3, 7, 2};
int sum;
double mean;
ex_0114_AccumulateStats(values, 3, &sum, &mean);
```

**`sum`** is now **`6`** and **`mean`** is now **`2.0`**.

```c
int values[] = {-4, -1};
int sum;
double mean;
ex_0114_AccumulateStats(values, 2, &sum, &mean);
```

**`sum`** is now **`-5`** and **`mean`** is now **`-2.5`**.

```c
int values[] = {5};
int sum;
double mean;
ex_0114_AccumulateStats(values, 1, &sum, &mean);
```

**`sum`** is now **`5`** and **`mean`** is now **`5.0`**.

## Constraints

- **`count`** is always at least **`1`**.
- The sum of the first **`count`** values fits in an **`int`**.
