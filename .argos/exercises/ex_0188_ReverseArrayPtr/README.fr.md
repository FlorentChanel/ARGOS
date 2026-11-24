<!-- Generated at publication from metadata.json — do not edit by hand -->

# 0188 — Reverse Array Ptr

**Langage :** C

**Difficulté :** 🟡 moyen

**Compétences testées :**
- pointeurs / déréférencement

## Tâche

Implémentez **`ex_0188_ReverseArrayPtr`** pour qu'elle copie les éléments d'un
tableau d'entiers dans un second tableau, dans l'ordre inverse. Le tableau
source n'est pas modifié.

## Signature

**`ex_0188_ReverseArrayPtr`** prend trois paramètres : **`source`** de type
pointeur sur un **`int`** constant (le premier élément du tableau à copier),
**`destination`** de type pointeur sur un **`int`** (le premier élément du
tableau qui reçoit la copie), et **`size`** de type **`int`** (le nombre
d'éléments de chaque tableau). Elle ne retourne rien.

## Exemples

```c
int source[] = {1, 2, 3, 4, 5};
int destination[5];
ex_0188_ReverseArrayPtr(source, destination, 5);
```

**`destination`** vaut maintenant **`{5, 4, 3, 2, 1}`** et **`source`** vaut
toujours **`{1, 2, 3, 4, 5}`**.

```c
int source[] = {-3, 8, 0, 12};
int destination[4];
ex_0188_ReverseArrayPtr(source, destination, 4);
```

**`destination`** vaut maintenant **`{12, 0, 8, -3}`**.

```c
int source[] = {7, 7, 2};
int destination[3];
ex_0188_ReverseArrayPtr(source, destination, 3);
```

**`destination`** vaut maintenant **`{2, 7, 7}`**.

```c
int source[] = {42};
int destination[1];
ex_0188_ReverseArrayPtr(source, destination, 1);
```

**`destination`** vaut maintenant **`{42}`**.

## Contraintes

- **`size`** vaut au moins **`1`**.
- **`source`** et **`destination`** ne se chevauchent pas.
