<!-- Generated at publication from metadata.json — do not edit by hand -->

# 0111 — Div Mod

**Langage :** C

**Difficulté :** 🟡 moyen

**Compétences testées :**
- passage par adresse

## Tâche

Implémentez **`ex_0111_DivMod`** pour qu'elle calcule le quotient entier et le
reste de la division de **`dividend`** par **`divisor`**, et les range dans les
deux variables entières dont les adresses sont passées en paramètres.

## Signature

**`ex_0111_DivMod`** prend quatre paramètres : **`dividend`** et **`divisor`** de
type **`int`**, puis **`quotient`** et **`remainder`** de type pointeur sur un
**`int`**. Elle ne retourne rien.

## Exemples

```c
int q = 0;
int r = 0;
ex_0111_DivMod(17, 5, &q, &r);
```

**`q`** vaut maintenant **`3`** et **`r`** vaut maintenant **`2`**.

```c
int q = 0;
int r = 0;
ex_0111_DivMod(20, 4, &q, &r);
```

**`q`** vaut maintenant **`5`** et **`r`** vaut maintenant **`0`**.

```c
int q = 0;
int r = 0;
ex_0111_DivMod(3, 8, &q, &r);
```

**`q`** vaut maintenant **`0`** et **`r`** vaut maintenant **`3`**.

```c
int q = 0;
int r = 0;
ex_0111_DivMod(-17, 5, &q, &r);
```

**`q`** vaut maintenant **`-3`** et **`r`** vaut maintenant **`-2`**.

## Contraintes

- **`divisor`** ne vaut jamais **`0`**.
- Le quotient tient toujours dans un **`int`** : **`dividend`** ne vaut jamais
  **`INT_MIN`** quand **`divisor`** vaut **`-1`**.
