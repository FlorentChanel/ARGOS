<!-- Generated at publication from metadata.json — do not edit by hand -->

# 0023 — Compare Array

**Langage :** C

**Difficulté :** 🟢 facile

**Compétences testées :**
- tableaux 1D

## Tâche

Implémentez **`ex_0023_CompareArray`** pour qu'elle compare les
**`nb_vals`** premiers éléments de deux tableaux d'entiers et renvoie
**`true`** s'ils sont identiques, et **`false`** sinon.

## Signature

**`ex_0023_CompareArray`** prend trois paramètres, dans cet ordre : deux
tableaux d'**`int`** **`array1`** et **`array2`**, et un **`int`**
**`nb_vals`**, le nombre d'éléments à comparer. Elle renvoie un
**`bool`**.

## Exemples

Pour les tableaux suivants :

```c
int array1[] = {1, 2, 3, 4, 4};
int array2[] = {1, 2, 3, 4, 5};
```

| Appel                                         | valeur retournée |
|-----------------------------------------------|------------------|
| **`ex_0023_CompareArray(array1, array2, 0)`** | true             |
| **`ex_0023_CompareArray(array1, array2, 4)`** | true             |
| **`ex_0023_CompareArray(array1, array2, 5)`** | false            |
