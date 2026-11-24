<!-- Generated at publication from metadata.json — do not edit by hand -->

# 0185 — Array Sum Ptr

**Langage :** C

**Difficulté :** 🟡 moyen

**Compétences testées :**
- pointeurs / déréférencement

## Tâche

Implémentez **`ex_0185_ArraySumPtr`** pour qu'elle retourne la somme des éléments
d'un tableau d'entiers dont l'adresse est passée en paramètre.

## Signature

**`ex_0185_ArraySumPtr`** prend deux paramètres : **`values`**, un pointeur sur le
premier élément d'un tableau de **`int`** (non modifié), et **`size`** de type
**`int`**, le nombre d'éléments du tableau. Elle retourne la somme des éléments
sous forme d'un **`int`**.

## Exemples

```c
int data[] = {1, 2, 3, 4};
int sum = ex_0185_ArraySumPtr(data, 4);
```

**`sum`** vaut **`10`**.

```c
int data[] = {-5, 8, -3, 2, 7};
int sum = ex_0185_ArraySumPtr(data, 5);
```

**`sum`** vaut **`9`**.

```c
int data[] = {42};
int sum = ex_0185_ArraySumPtr(data, 1);
```

**`sum`** vaut **`42`**.

```c
int data[] = {10, 20, 30, 40};
int sum = ex_0185_ArraySumPtr(data + 1, 2);
```

**`sum`** vaut **`50`**.

```c
int data[] = {7};
int sum = ex_0185_ArraySumPtr(data, 0);
```

**`sum`** vaut **`0`**.

## Contraintes

- **`size`** vaut au moins 0 et **`values`** a au moins **`size`** éléments.
- Chaque somme partielle et la somme tiennent dans un **`int`**.
