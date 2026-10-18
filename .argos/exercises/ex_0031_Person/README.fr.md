<!-- Generated at publication from metadata.json — do not edit by hand -->

# 0031 — Person

**Langage :** C

**Difficulté :** 🟡 moyen

**Compétences testées :**
- tableaux de structures
- chaînes de caractères

## Tâche

1. Créez un type **`Person`** pour une personne, caractérisée par son
   nom (20 caractères maximum), son prénom (20 caractères maximum) et son
   année de naissance.
2. Implémentez **`ex_0031_Person`** pour qu'elle :
   1. déclare un tableau de 10 personnes et l'initialise avec les données
      des sept personnes suivantes :

      ```
      "Knuth", "Donald", 1938
      "Kernighan", "Brian", 1942
      "Ritchie", "Dennis", 1941
      "Thompson", "Ken", 1943
      "Minsky", "Marvin", 1927
      "Dijkstra", "Edsger", 1930
      "Stroustrup", "Bjarne", 1950
      ```

   2. affiche le nombre de personnes enregistrées ;
   3. affiche toutes les personnes âgées de moins de 80 ans ;
   4. affiche les noms qui sont en tête/en fin de classement selon l'ordre
      alphanumérique (le plus proche de « AAA » / le plus proche de « ZZZ »).

## Signature

**`ex_0031_Person`** ne prend aucun paramètre et ne renvoie rien
(**`void`**).

## Sortie attendue

```
7 Persons
Persons less than 80 years old:
Brian Kernighan 78 years
Dennis Ritchie 79 years
Ken Thompson 77 years
Bjarne Stroustrup 70 years

Alphabetic order:
The first is: Dijkstra
The last is: Thompson
```

## Contraintes

- Il faut considérer que nous sommes en 2020.
- Utilisez la fonction **`strcmp()`** pour comparer les noms.
- L'affichage se termine par un retour à la ligne.
