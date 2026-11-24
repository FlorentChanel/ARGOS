<!-- Generated at publication from metadata.json — do not edit by hand -->

# 0115 — Clamp Inplace

**Langage :** C

**Difficulté :** 🟡 moyen

**Compétences testées :**
- passage par adresse

## Tâche

Implémentez **`ex_0115_ClampInplace`** pour qu'elle borne la variable entière dont
l'adresse est passée en paramètre à l'intervalle [**`min`**, **`max`**] : une
valeur inférieure à **`min`** devient **`min`**, une valeur supérieure à
**`max`** devient **`max`**, une valeur comprise dans l'intervalle reste inchangée.

## Signature

**`ex_0115_ClampInplace`** prend trois paramètres : **`value`** de type pointeur
sur un **`int`**, puis **`min`** et **`max`** de type **`int`**. Elle ne retourne
rien.

## Exemples

```c
int a = 15;
ex_0115_ClampInplace(&a, 0, 10);
```

**`a`** vaut maintenant **`10`**.

```c
int b = -3;
ex_0115_ClampInplace(&b, 0, 10);
```

**`b`** vaut maintenant **`0`**.

```c
int c = 7;
ex_0115_ClampInplace(&c, 0, 10);
```

**`c`** vaut toujours **`7`**.

```c
int d = -20;
ex_0115_ClampInplace(&d, -10, -5);
```

**`d`** vaut maintenant **`-10`**.

## Contraintes

- **`min`** est toujours inférieur ou égal à **`max`**.
