<!-- Generated at publication from metadata.json — do not edit by hand -->

# 0190 — Reverse Inplace Ptr

**Langage :** C

**Difficulté :** 🟢 facile

**Compétences testées :**
- arithmétique des pointeurs

## Tâche

Implémentez **`ex_0190_ReverseInplacePtr`** pour qu'elle inverse l'ordre des
éléments d'un tableau d'entiers, en place : le tableau lui-même est modifié,
aucun autre tableau n'est utilisé, en déplaçant deux pointeurs l'un vers l'autre.

## Signature

**`ex_0190_ReverseInplacePtr`** prend deux paramètres : **`array`** de type
pointeur sur un **`int`** (le premier élément du tableau à inverser) et
**`size`** de type **`int`** (le nombre d'éléments du tableau). Elle ne
retourne rien.

## Exemples

```c
int array[] = {1, 2, 3, 4, 5};
ex_0190_ReverseInplacePtr(array, 5);
```

**`array`** vaut maintenant **`{5, 4, 3, 2, 1}`**.

```c
int array[] = {-3, 8, 0, 12};
ex_0190_ReverseInplacePtr(array, 4);
```

**`array`** vaut maintenant **`{12, 0, 8, -3}`**.

```c
int array[] = {7, 7, 2};
ex_0190_ReverseInplacePtr(array, 3);
```

**`array`** vaut maintenant **`{2, 7, 7}`**.

```c
int array[] = {42};
ex_0190_ReverseInplacePtr(array, 1);
```

**`array`** vaut toujours **`{42}`**.

## Contraintes

- **`size`** vaut au moins **`1`**.
- N'utilisez pas l'opérateur **`[]`**.
