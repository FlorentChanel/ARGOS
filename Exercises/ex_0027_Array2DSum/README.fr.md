<!-- Generated at publication from metadata.json — do not edit by hand -->

# 0027 — Array 2D Sum

**Langage :** C

**Difficulté :** 🔴 difficile

**Compétences testées :**
- tableaux 2D / matrices
- entrées-sorties formatées

## Tâche

Implémentez **`ex_0027_Array2DSum`** pour qu'elle :

1. déclare un tableau d'entiers (taille maximale : 50 lignes et
   50 colonnes)
2. lise les tailles (nombre de lignes et nombre de colonnes) au clavier
3. remplisse le tableau avec des valeurs entrées au clavier
4. affiche la somme de tous ses éléments

## Signature

**`ex_0027_Array2DSum`** ne prend aucun paramètre et ne retourne rien (**`void`**).

## Exemples

Dans les exemples, le texte qui suit chaque invite est saisi par l'utilisateur ;
chaque invite se termine par une espace, sans retour à la ligne.

```
Nb lines (max.50): a
Nb lines (max.50): -1
Nb lines (max.50): 2
Nb columns (max.50): a
Nb columns (max.50): -1
Nb columns (max.50): 2
array[0][0]: 1
array[0][1]: 2
array[1][0]: 3
array[1][1]: 4
Total sum: 10
```

```
Nb lines (max.50): 0
Nb columns (max.50): 9
Total sum: 0
```

```
Nb lines (max.50): 9
Nb columns (max.50): 0
Total sum: 0
```

```
Nb lines (max.50): 0
Nb columns (max.50): 0
Total sum: 0
```

## Contraintes

- Gérez les erreurs de saisie : redemandez avec la même invite tant qu'une
  taille ou une valeur valide n'est pas lue.
- Une taille valide est un entier de 0 à 50 inclus.
- Après chaque **`scanf`**, videz **`stdin`** : ignorez le reste de la ligne,
  jusqu'à **`\n`** ou **`EOF`** (voir [Reading from stdin](https://github.com/HE-Arc/ARGOS#reading-from-stdin)).
- L'affichage se termine par un retour à la ligne.
