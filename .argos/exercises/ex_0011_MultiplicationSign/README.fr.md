<!-- Generated at publication from metadata.json — do not edit by hand -->

# 0011 — Multiplication Sign

**Langage :** C

**Difficulté :** 🟡 moyen

**Compétences testées :**
- conditions (if / switch)

## Tâche

Complétez **`ex_0011_MultiplicationSign`** pour qu'elle lise deux valeurs
entières (**`a`** et **`b`**) au clavier et affiche le signe du produit
(positif, négatif ou zéro) de **`a`** et **`b`** **sans faire la
multiplication**.

## Signature

```c
void ex_0011_MultiplicationSign(void);
```

## Exemples

```
Please enter 2 integers: 1 2
1 * 2 > 0
```

```
Please enter 2 integers: 0 0
0 * 0 = 0
```

```
Please enter 2 integers: a b
Please enter 2 integers: b 1
Please enter 2 integers: -1 3
-1 * 3 < 0
```

## Contraintes

- Gérez les erreurs de saisie : redemandez tant que deux entiers ne sont pas lus.
- Après chaque **`scanf`**, videz **`stdin`** : ignorez le reste de la ligne,
  jusqu'à **`\n`** ou **`EOF`** (voir [Reading from stdin](https://github.com/HE-Arc/ARGOS#reading-from-stdin)).
- L'affichage se termine par un retour à la ligne.
