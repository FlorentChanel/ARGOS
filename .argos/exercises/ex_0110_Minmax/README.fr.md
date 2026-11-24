<!-- Generated at publication from metadata.json — do not edit by hand -->

# 0110 — Minmax

**Langage :** C

**Difficulté :** 🟢 facile

**Compétences testées :**
- passage par adresse

## Tâche

Implémentez **`ex_0110_Minmax`** pour qu'elle range le plus petit et le plus grand
de trois entiers dans les deux variables dont les adresses sont passées en
paramètres.

## Signature

**`ex_0110_Minmax`** prend cinq paramètres : **`a`**, **`b`** et **`c`** de type
**`int`**, puis **`min`** et **`max`**, chacun de type pointeur sur un **`int`**.
Elle ne retourne rien.

## Exemples

```c
int lo;
int hi;
ex_0110_Minmax(4, 9, 2, &lo, &hi);
```

**`lo`** vaut maintenant **`2`** et **`hi`** vaut maintenant **`9`**.

```c
int lo;
int hi;
ex_0110_Minmax(-3, 0, -8, &lo, &hi);
```

**`lo`** vaut maintenant **`-8`** et **`hi`** vaut maintenant **`0`**.

```c
int lo;
int hi;
ex_0110_Minmax(5, 5, 1, &lo, &hi);
```

**`lo`** vaut maintenant **`1`** et **`hi`** vaut maintenant **`5`**.

```c
int lo;
int hi;
ex_0110_Minmax(7, 7, 7, &lo, &hi);
```

**`lo`** et **`hi`** valent maintenant tous deux **`7`**.
