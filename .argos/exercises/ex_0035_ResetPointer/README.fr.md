<!-- Generated at publication from metadata.json — do not edit by hand -->

# 0035 — Reset Pointer

**Langage :** C

**Difficulté :** 🟡 moyen

**Compétences testées :**
- pointeurs / déréférencement

## Tâche

Implémentez **`ex_0035_ResetPointer`** pour qu'elle mette à **`NULL`** le
pointeur sur **`int`** dont l'adresse est passée en paramètre.

## Signature

**`ex_0035_ResetPointer`** prend un paramètre **`pointer`** de type
pointeur sur un pointeur sur un **`int`**. Elle ne retourne rien.

## Exemples

```c
int x = 42;
int *p = &x;
ex_0035_ResetPointer(&p);
```

**`p`** vaut maintenant **`NULL`**, **`x`** vaut toujours **`42`**.

```c
int values[3] = {1, 2, 3};
int *q = &values[2];
ex_0035_ResetPointer(&q);
```

**`q`** vaut maintenant **`NULL`**, **`values`** vaut toujours **`{1, 2, 3}`**.

```c
int *r = NULL;
ex_0035_ResetPointer(&r);
```

**`r`** vaut toujours **`NULL`**.
