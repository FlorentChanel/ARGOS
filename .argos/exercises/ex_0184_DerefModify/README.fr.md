<!-- Generated at publication from metadata.json — do not edit by hand -->

# 0184 — Deref Modify

**Langage :** C

**Difficulté :** 🟡 moyen

**Compétences testées :**
- pointeurs / déréférencement

## Tâche

Implémentez **`ex_0184_DerefModify`** pour qu'elle ajoute **`delta`** à la
variable entière dont l'adresse est passée en paramètre.

## Signature

**`ex_0184_DerefModify`** prend deux paramètres : **`value`** de type pointeur
sur un **`int`**, et **`delta`** de type **`int`**. Elle ne retourne rien.

## Exemples

```c
int a = 10;
ex_0184_DerefModify(&a, 5);
```

**`a`** vaut maintenant **`15`**.

```c
int b = 3;
ex_0184_DerefModify(&b, -8);
```

**`b`** vaut maintenant **`-5`**.

```c
int c = -4;
ex_0184_DerefModify(&c, 0);
```

**`c`** vaut toujours **`-4`**.

```c
int d = 1;
ex_0184_DerefModify(&d, 2);
ex_0184_DerefModify(&d, 2);
```

**`d`** vaut maintenant **`5`**.
