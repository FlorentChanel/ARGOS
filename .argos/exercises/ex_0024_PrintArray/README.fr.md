<!-- Generated at publication from metadata.json — do not edit by hand -->

# 0024 — Print Array

**Langage :** C

**Difficulté :** 🟢 facile

**Compétences testées :**
- tableaux 1D

## Tâche

Implémentez **`ex_0024_PrintArray`** pour qu'elle affiche à l'écran un
tableau d'entiers.

## Signature

**`ex_0024_PrintArray`** prend deux paramètres, dans cet ordre : un
tableau d'**`int`** **`array`** et un **`int`** **`size`**, le nombre
d'éléments du tableau. Elle ne renvoie rien (**`void`**).

## Exemples

Pour le tableau suivant :

```c
int array[] = {1, 2, 3, 4, 5};
```

| Appel                               | affichage       |
|-------------------------------------|-----------------|
| **`ex_0024_PrintArray(array, 0)`**  | *rien*          |
| **`ex_0024_PrintArray(array, 4)`**  | **`1 2 3 4`**   |
| **`ex_0024_PrintArray(array, 5)`**  | **`1 2 3 4 5`** |

> [!WARNING]
> Chaque élément du tableau est suivi d'un espace, **sauf le dernier**.
> De plus, **il ne faut pas** terminer l'affichage par un **`\n`**.
