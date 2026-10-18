<!-- Generated at publication from metadata.json — do not edit by hand -->

# 0031 — Person

**Language:** C

**Difficulty:** 🟡 medium

**Tested skills:**
- arrays of structures
- strings

## Task

1. Create a **`Person`** type for a person, characterized by their last
   name (20 characters maximum), first name (20 characters maximum) and
   birth year.
2. Implement **`ex_0031_Person`** so that it:
   1. declares an array of 10 persons and initializes it with the data of
      the seven following persons:

      ```
      "Knuth", "Donald", 1938
      "Kernighan", "Brian", 1942
      "Ritchie", "Dennis", 1941
      "Thompson", "Ken", 1943
      "Minsky", "Marvin", 1927
      "Dijkstra", "Edsger", 1930
      "Stroustrup", "Bjarne", 1950
      ```

   2. prints the number of persons stored;
   3. prints all the persons less than 80 years old;
   4. prints the last names that come first/last in alphanumeric order
      (closest to "AAA" / closest to "ZZZ").

## Signature

**`ex_0031_Person`** takes no parameter and returns nothing
(**`void`**).

## Expected output

```
7 Persons
Persons less than 80 years old:
Brian Kernighan 78 years
Dennis Ritchie 79 years
Ken Thompson 77 years
Bjarne Stroustrup 70 years

Alphabetic order:
The first is: Dijkstra
The last is: Thompson
```

## Constraints

- Consider that the current year is 2020.
- Use the **`strcmp()`** function to compare the names.
- The output ends with a newline.
