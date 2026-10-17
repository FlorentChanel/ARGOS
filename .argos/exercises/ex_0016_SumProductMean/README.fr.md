<!-- Generated at publication from metadata.json — do not edit by hand -->

# 0016 — Sum Product Mean

**Langage :** C

**Difficulté :** 🔴 difficile

**Compétences testées :**
- boucle for
- entrées-sorties formatées

## Tâche

Complétez **`ex_0016_SumProductMean`** pour qu'elle :

1. lise **`N`** nombres entiers au clavier et affiche leur somme, leur
   produit et leur moyenne — choisissez un type approprié pour les valeurs
   à afficher, et utilisez la boucle la plus appropriée ;
2. répète l'introduction du nombre **`N`** jusqu'à ce que **`N`** ait une
   valeur entre 1 et 15.

## Signature

```c
void ex_0016_SumProductMean(void);
```

## Sortie attendue

La session console ressemble à ceci (le texte après chaque invite, **`16`**, **`0`**,
**`-1`**, **`3`**, **`a`**, **`1`**, **`b`**, **`2`**, **`c`** et **`3`**, est tapé par l'utilisateur) :

```
Number of values to read: 16
Number of values to read: 0
Number of values to read: -1
Number of values to read: 3
1. number: a
1. number: 1
2. number: b
2. number: 2
3. number: c
3. number: 3
Sum = 6
Product = 6
Mean = 2.0000
```

## Contraintes

- Les tests utilisent des entiers entre -4 et 4 : la somme et le produit tiennent
  toujours dans un **`int`** et s'affichent comme des entiers.
- Affichez les réels avec 4 chiffres après la virgule.
- Gérez les erreurs de saisie : redemandez tant qu'un nombre valide n'est pas lu.
- Après chaque **`scanf`**, videz **`stdin`** : ignorez le reste de la ligne,
  jusqu'à **`\n`** ou **`EOF`** (voir [Reading from stdin](https://github.com/HE-Arc/ARGOS#reading-from-stdin)).
- L'affichage se termine par un retour à la ligne.
