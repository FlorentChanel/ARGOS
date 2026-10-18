<!-- Generated at publication from metadata.json — do not edit by hand -->

# 0029 — Time

**Langage :** C

**Difficulté :** 🟡 moyen

**Compétences testées :**
- structures (struct)
- fonctions (paramètres par valeur)

## Tâche

Définissez, avec un **`typedef`**, une structure **`Time`** qui mémorise
le temps d'un marathon (hh:mm:ss). Implémentez ensuite les trois
fonctions :

1. **`ex_0029_InitTime`** prend 3 entiers (heures, minutes, secondes)
   passés en paramètres et retourne une structure **`Time`**.
2. **`ex_0029_PrintTime`** prend une structure **`Time`** en paramètre et
   affiche le temps associé.
3. **`ex_0029_Time`** crée une structure **`Time`** contenant 5 heures,
   3 minutes et 17 secondes en utilisant **`ex_0029_InitTime`** et
   l'affiche en utilisant **`ex_0029_PrintTime`**.

## Signature

**`Time`** est un type structure à trois membres : **`hh`** (heures),
**`mm`** (minutes) et **`ss`** (secondes).

- **`ex_0029_InitTime`** prend trois paramètres **`int`**, dans cet
  ordre : les heures, les minutes et les secondes. Elle retourne un
  **`Time`**.
- **`ex_0029_PrintTime`** prend un paramètre **`Time`** et ne retourne
  rien.
- **`ex_0029_Time`** ne prend aucun paramètre et ne retourne rien.

## Sortie attendue

```c
Time t = ex_0029_InitTime(5, 3, 17);
ex_0029_PrintTime(t);
```

affiche **`05:03:17`**.

## Contraintes

- Les entrées sont toujours valides : heures de 0 à 99, minutes et
  secondes de 0 à 59.
- L'affichage se termine par un retour à la ligne.
