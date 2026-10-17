<!-- Generated at publication from metadata.json — do not edit by hand -->

# 0025 — Fill Array

**Langage :** C

**Difficulté :** 🟢 facile

**Compétences testées :**
- tableaux 1D
- entrées-sorties formatées

## Tâche

Implémentez **`ex_0025_FillArray`** pour qu'elle remplisse un tableau
d'entiers passé en paramètre avec des valeurs saisies au clavier par
l'utilisateur. On s'arrête quand l'utilisateur entre une valeur négative,
quand le tableau contient **`max_capacity`** valeurs, ou à la fin de
l'entrée ; rien n'est lu
quand **`max_capacity`** vaut 0 ou est négatif. La fonction retourne le
nombre de valeurs correctes saisies.

## Signature

**`ex_0025_FillArray`** prend deux paramètres, dans cet ordre : un tableau
d'**`int`** **`array`** et sa capacité **`int`** **`max_capacity`**. Elle
retourne un **`int`**.

## Exemples

**`ex_0025_FillArray(array, -1)`** et **`ex_0025_FillArray(array, 0)`**
ne font rien et retournent 0.

Pour le tableau :

```c
int array[] = {-2, -2, -2, -2};
```

**`ex_0025_FillArray(array, 4)`** avec les saisies au clavier

```
a
b
1
-1
```

change le tableau en **`{1, -2, -2, -2}`** et retourne 1.

**`ex_0025_FillArray(array, 4)`** avec les saisies au clavier

```
2
2
-2
```

change le tableau en **`{2, 2, -2, -2}`** et retourne 2.

**`ex_0025_FillArray(array, 4)`** avec les saisies au clavier

```
3
3
-2
```

change le tableau en **`{3, 3, -2, -2}`** et retourne 2.

## Contraintes

- Gérez les erreurs de saisie : les entrées non numériques sont ignorées.
- Après chaque **`scanf`**, videz **`stdin`** : ignorez le reste de la ligne,
  jusqu'à **`\n`** ou **`EOF`** (voir [Reading from stdin](https://github.com/HE-Arc/ARGOS#reading-from-stdin)).
