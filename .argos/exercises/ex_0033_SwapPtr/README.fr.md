<!-- Generated at publication from metadata.json — do not edit by hand -->

# 0033 — Swap Ptr

**Langage :** C

**Difficulté :** 🟢 facile

**Compétences testées :**
- passage par adresse

## Tâche

Implémentez **`ex_0033_SwapPtr`** pour qu'elle échange les valeurs des deux
variables entières dont les adresses sont passées en paramètres.

## Signature

**`ex_0033_SwapPtr`** prend deux paramètres **`a`** et **`b`**, chacun de type
pointeur sur un **`int`**. Elle ne retourne rien.

## Exemples

```c
int x = 3;
int y = 8;
ex_0033_SwapPtr(&x, &y);
```

**`x`** vaut maintenant **`8`** et **`y`** vaut maintenant **`3`**.

```c
int x = -5;
int y = 0;
ex_0033_SwapPtr(&x, &y);
```

**`x`** vaut maintenant **`0`** et **`y`** vaut maintenant **`-5`**.

```c
int x = 7;
int y = 7;
ex_0033_SwapPtr(&x, &y);
```

**`x`** et **`y`** valent toujours **`7`**.
