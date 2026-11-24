<!-- Generated at publication from metadata.json — do not edit by hand -->

# 0186 — Find Max Ptr

**Langage :** C

**Difficulté :** 🟡 moyen

**Compétences testées :**
- pointeurs / déréférencement

## Tâche

Implémentez **`ex_0186_FindMaxPtr`** pour qu'elle retourne l'adresse du plus
grand élément d'un tableau d'entiers. Lorsque la plus grande valeur apparaît
plusieurs fois, elle retourne l'adresse de sa première occurrence.

## Signature

**`ex_0186_FindMaxPtr`** prend deux paramètres : **`values`** de type pointeur
sur un **`int`** (le premier élément du tableau), et **`size`** de type
**`int`** (le nombre d'éléments). Elle retourne un pointeur sur un **`int`**.

## Exemples

```c
int values[] = {3, 8, 1, 6};
int *p = ex_0186_FindMaxPtr(values, 4);
```

**`p`** vaut **`&values[1]`** et **`*p`** vaut **`8`**.

```c
int values[] = {-7, -2, -9};
int *p = ex_0186_FindMaxPtr(values, 3);
```

**`p`** vaut **`&values[1]`** et **`*p`** vaut **`-2`**.

```c
int values[] = {5, 9, 2, 9};
int *p = ex_0186_FindMaxPtr(values, 4);
```

**`p`** vaut **`&values[1]`** et **`*p`** vaut **`9`**.

```c
int values[] = {4};
int *p = ex_0186_FindMaxPtr(values, 1);
```

**`p`** vaut **`&values[0]`** et **`*p`** vaut **`4`**.

```c
int values[] = {2, 7, 4};
*ex_0186_FindMaxPtr(values, 3) = 0;
```

**`values`** vaut maintenant **`{2, 0, 4}`**.

## Contraintes

- **`size`** vaut au moins **`1`**.
