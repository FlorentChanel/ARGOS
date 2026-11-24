<!-- Generated at publication from metadata.json — do not edit by hand -->

# 0032 — Copy Arrays

**Langage :** C

**Difficulté :** 🟡 moyen

**Compétences testées :**
- passage par adresse
- tableaux 1D

## Tâche

Implémentez **`ex_0032_CopyArrays`** pour qu'elle copie les **`n`** premiers
éléments d'un tableau d'entiers source dans un tableau d'entiers destination.
Le tableau source n'est pas modifié, et les éléments du tableau destination
au-delà des **`n`** premiers restent inchangés.

## Signature

**`ex_0032_CopyArrays`** prend trois paramètres, dans cet ordre : le tableau
source **`src`** (pointeur sur un **`const int`**), le tableau destination
**`dst`** (pointeur sur un **`int`**) et le nombre d'éléments à copier **`n`**
(**`int`**). Elle ne retourne rien.

## Exemples

```c
int src[] = {4, -1, 7, 0, 12};
int dst[] = {0, 0, 0, 0, 0};
ex_0032_CopyArrays(src, dst, 5);
```

**`dst`** vaut maintenant **`{4, -1, 7, 0, 12}`** et **`src`** vaut toujours
**`{4, -1, 7, 0, 12}`**.

```c
int src[] = {9, 8, 7, 6};
int dst[] = {1, 1, 1, 1, 1, 1};
ex_0032_CopyArrays(src, dst, 3);
```

**`dst`** vaut maintenant **`{9, 8, 7, 1, 1, 1}`**.

```c
int src[] = {5, 5};
int dst[] = {3, 3};
ex_0032_CopyArrays(src, dst, 0);
```

**`dst`** vaut toujours **`{3, 3}`**.

## Contraintes

- **`n`** vaut au moins 0 et les deux tableaux ont au moins **`n`** éléments.
- Les deux tableaux ne se chevauchent pas.
