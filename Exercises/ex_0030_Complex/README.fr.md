<!-- Generated at publication from metadata.json — do not edit by hand -->

# 0030 — Complex

**Langage :** C

**Difficulté :** 🔴 difficile

**Compétences testées :**
- structures (struct)
- fonctions (paramètres par valeur)

## Tâche

Implémentez le type et les fonctions qui gèrent des nombres complexes :

1. Définissez le type **`Complex`** avec 2 membres de type **`double`** :
   **`real`** et **`imaginary`**.
2. **`ex_0030_InputComplex`** lit un nombre complexe, en n'acceptant que
   le format **`(r,i)`**, et retourne une structure **`Complex`**. Avant
   chaque tentative de lecture, elle affiche l'invite montrée dans l'exemple
   ci-dessous.
3. **`ex_0030_SumComplex`** et **`ex_0030_DiffComplex`** calculent la
   somme et la différence de deux nombres complexes stockés dans une
   structure **`Complex`**.

   $(a_1 + i b_1) + (a_2 + i b_2) = (a_1+a_2) + i(b_1+b_2)$

   $(a_1 + i b_1) - (a_2 + i b_2) = (a_1-a_2) + i(b_1-b_2)$

4. **`ex_0030_PrintComplex`** affiche un nombre complexe sous la forme
   suivante, suivi d'un retour à la ligne : **`5.00 + -3.00i`**.
5. **`ex_0030_Complex`** lit deux nombres complexes, calcule leur somme
   et leur différence et affiche les résultats, en utilisant les
   fonctions écrites dans les points précédents.

## Signature

- **`ex_0030_InputComplex`** ne prend aucun paramètre et retourne un
  **`Complex`**.
- **`ex_0030_SumComplex`** et **`ex_0030_DiffComplex`** prennent chacune
  deux paramètres de type **`Complex`** et retournent un **`Complex`**.
- **`ex_0030_PrintComplex`** prend un paramètre de type **`Complex`** et
  ne retourne rien (**`void`**).
- **`ex_0030_Complex`** ne prend aucun paramètre et ne retourne rien
  (**`void`**).

## Sortie attendue

```
Please enter a complex number (r,i): a
Please enter a complex number (r,i): -1
Please enter a complex number (r,i): (1, 1)
Please enter a complex number (r,i): (2, 3)

Sum = 3.00 + 4.00i

Diff = -1.00 + -2.00i
```

À lui seul, un appel à **`ex_0030_PrintComplex`** avec une partie réelle de
**`5`** et une partie imaginaire de **`-3`** affiche la ligne suivante,
suivie d'un retour à la ligne :

```
5.00 + -3.00i
```

## Contraintes

- Gérez les erreurs de saisie : redemandez tant que le format **`(r,i)`** n'est pas lu.
- Les espaces et les tabulations sont acceptés autour des nombres et autour des parenthèses ;
  tout autre caractère hors du format **`(r,i)`** rend la saisie invalide.
- Après chaque **`scanf`**, videz **`stdin`** : ignorez le reste de la ligne,
  jusqu'à **`\n`** ou **`EOF`** (voir [Reading from stdin](https://github.com/HE-Arc/ARGOS#reading-from-stdin)).
