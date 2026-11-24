<!-- Generated at publication from metadata.json — do not edit by hand -->

# 0034 — Reset

**Langage :** C

**Difficulté :** 🟢 facile

**Compétences testées :**
- pointeurs / déréférencement

## Tâche

Implémentez **`ex_0034_Reset`** pour qu'elle remette à zéro la variable
entière dont l'adresse est passée en paramètre.

## Signature

**`ex_0034_Reset`** prend un paramètre **`value`** de type pointeur sur
un **`int`**. Elle ne retourne rien.

## Exemples

```c
int a = 42;
ex_0034_Reset(&a);
```

**`a`** vaut maintenant **`0`**.

```c
int b = -7;
ex_0034_Reset(&b);
```

**`b`** vaut maintenant **`0`**.

```c
int c = 0;
ex_0034_Reset(&c);
```

**`c`** vaut toujours **`0`**.
