<!-- Generated at publication from metadata.json — do not edit by hand -->

# 0114 — Accumulate Stats

**Langage :** C

**Difficulté :** 🟡 moyen

**Compétences testées :**
- passage par adresse

## Tâche

Implémentez **`ex_0114_AccumulateStats`** pour qu'elle calcule la somme et la
moyenne des **`count`** premiers entiers du tableau **`values`**, et les range
dans les deux variables dont les adresses sont passées en paramètres.

## Signature

**`ex_0114_AccumulateStats`** prend quatre paramètres : **`values`**, un tableau
d'**`int`** qu'elle ne modifie pas, **`count`** de type **`int`**, puis **`sum`**
de type pointeur sur un **`int`** et **`mean`** de type pointeur sur un
**`double`**. Elle ne retourne rien.

## Exemples

```c
int values[] = {1, 2, 3, 4};
int sum;
double mean;
ex_0114_AccumulateStats(values, 4, &sum, &mean);
```

**`sum`** vaut maintenant **`10`** et **`mean`** vaut maintenant **`2.5`**.

```c
int values[] = {-3, 7, 2};
int sum;
double mean;
ex_0114_AccumulateStats(values, 3, &sum, &mean);
```

**`sum`** vaut maintenant **`6`** et **`mean`** vaut maintenant **`2.0`**.

```c
int values[] = {-4, -1};
int sum;
double mean;
ex_0114_AccumulateStats(values, 2, &sum, &mean);
```

**`sum`** vaut maintenant **`-5`** et **`mean`** vaut maintenant **`-2.5`**.

```c
int values[] = {5};
int sum;
double mean;
ex_0114_AccumulateStats(values, 1, &sum, &mean);
```

**`sum`** vaut maintenant **`5`** et **`mean`** vaut maintenant **`5.0`**.

## Contraintes

- **`count`** vaut toujours au moins **`1`**.
- La somme des **`count`** premières valeurs tient dans un **`int`**.
