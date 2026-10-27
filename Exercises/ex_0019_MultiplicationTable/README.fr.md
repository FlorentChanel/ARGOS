<!-- Generated at publication from metadata.json — do not edit by hand -->

# 0019 — Multiplication Table

**Langage :** C

**Difficulté :** 🟢 facile

**Compétences testées :**
- boucle for
- fonctions (paramètres par valeur)

## Tâche

Implémentez les deux fonctions qui saisissent un nombre compris entre deux
valeurs et affichent sa table de multiplication :

1. **`ex_0019_Read`** reçoit 2 paramètres entiers : une valeur min et une
   valeur max entre lesquelles le nombre saisi au clavier doit être
   compris, bornes min et max incluses. Son invite affiche ces deux valeurs
   dans la partie **`[min..max]`**. Elle retourne le nombre saisi.
2. **`ex_0019_MultiplicationTable`** affiche la table de multiplication
   demandée, de 1 à 10, selon les exemples ci-dessous.

Le **`main()`** fourni n'est constitué que de deux appels à ces fonctions.

## Signature

- **`ex_0019_Read`** prend deux paramètres de type **`int`** (les valeurs
  min et max) et retourne un **`int`**.
- **`ex_0019_MultiplicationTable`** prend un paramètre de type **`int`** et
  ne retourne rien (**`void`**).

## Sortie attendue

```
Please enter the multiplication table (in [1..12]): 0
Please enter the multiplication table (in [1..12]): 13
Please enter the multiplication table (in [1..12]): a
Please enter the multiplication table (in [1..12]): 5

MULTIPLICATION TABLE FOR 5
5 X 1 = 5
5 X 2 = 10
5 X 3 = 15
5 X 4 = 20
5 X 5 = 25
5 X 6 = 30
5 X 7 = 35
5 X 8 = 40
5 X 9 = 45
5 X 10 = 50
```

Appelée seule, **`ex_0019_MultiplicationTable(5)`** doit afficher ce qui
suit, en commençant par la ligne vide :

```

MULTIPLICATION TABLE FOR 5
5 X 1 = 5
5 X 2 = 10
5 X 3 = 15
5 X 4 = 20
5 X 5 = 25
5 X 6 = 30
5 X 7 = 35
5 X 8 = 40
5 X 9 = 45
5 X 10 = 50
```

## Contraintes

- Après chaque **`scanf`**, videz **`stdin`** : ignorez le reste de la ligne,
  jusqu'à **`\n`** ou **`EOF`** (voir [Reading from stdin](https://github.com/HE-Arc/ARGOS#reading-from-stdin)).
- **`ex_0019_MultiplicationTable`** ne reçoit qu'un numéro de table compris
  entre 1 et 12, bornes incluses.
- L'affichage se termine par un retour à la ligne.
