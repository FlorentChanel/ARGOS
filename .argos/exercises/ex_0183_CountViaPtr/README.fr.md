<!-- Generated at publication from metadata.json — do not edit by hand -->

# 0183 — Count Via Ptr

**Langage :** C

**Difficulté :** 🟢 facile

**Compétences testées :**
- pointeurs / déréférencement

## Tâche

Implémentez **`ex_0183_CountViaPtr`** pour qu'elle compte les éléments d'un
tableau d'entiers égaux à une valeur donnée, et range ce nombre dans la variable
dont l'adresse est passée en paramètre.

## Signature

**`ex_0183_CountViaPtr`** prend quatre paramètres : **`values`**, un tableau de
**`int`** (non modifié), **`size`** de type **`int`**, le nombre d'éléments de
**`values`**, **`target`** de type **`int`**, la valeur à compter, et **`count`**
de type pointeur sur un **`int`**. Elle ne retourne rien.

## Exemples

```c
int data[] = {3, 1, 3, 7, 3};
int n;
ex_0183_CountViaPtr(data, 5, 3, &n);
```

**`n`** vaut maintenant **`3`**.

```c
int data[] = {-2, 4, -2, 0};
int n;
ex_0183_CountViaPtr(data, 4, -2, &n);
```

**`n`** vaut maintenant **`2`**.

```c
int data[] = {5, 6, 8};
int n = 42;
ex_0183_CountViaPtr(data, 3, 9, &n);
```

**`n`** vaut maintenant **`0`**.

```c
int data[] = {1, 1, 1};
int n = 10;
ex_0183_CountViaPtr(data, 3, 1, &n);
```

**`n`** vaut maintenant **`3`**.

```c
int data[] = {7};
int n = 5;
ex_0183_CountViaPtr(data, 0, 7, &n);
```

**`n`** vaut maintenant **`0`**.
