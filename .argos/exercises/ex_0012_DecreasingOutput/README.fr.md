<!-- Generated at publication from metadata.json — do not edit by hand -->

# 0012 — Decreasing Output

**Langage :** C

**Difficulté :** 🟢 facile

**Compétences testées :**
- conditions (if / switch)

## Tâche

Complétez **`ex_0012_DecreasingOutput`** pour qu'elle affiche dans l'ordre
décroissant trois nombres introduits au clavier par l'utilisateur. Il
s'agit d'échanger le contenu des variables de manière à mettre la plus
grande valeur dans la première variable, la médiane dans la seconde et la
plus petite dans la troisième.

## Signature

```c
void ex_0012_DecreasingOutput(void);
```

## Exemples

```
Please enter 3 integers separated by commas: 1,2,3
The 3 integers sorted in decreasing order: 3, 2, 1
```

```
Please enter 3 integers separated by commas: 1,-2,0
The 3 integers sorted in decreasing order: 1, 0, -2
```

```
Please enter 3 integers separated by commas: a,1,2
Please enter 3 integers separated by commas: 1, -9, c
Please enter 3 integers separated by commas: 0,0,0
The 3 integers sorted in decreasing order: 0, 0, 0
```

## Contraintes

- Les trois entiers sont séparés par des virgules ; des espaces sont admis avant
  et après chaque virgule (par ex. **`1 , -2,0`**). Le reste de la ligne après le
  troisième entier est ignoré.
- Gérez les erreurs de saisie : redemandez tant que trois entiers ne sont pas lus.
- Après chaque **`scanf`**, videz **`stdin`** : ignorez le reste de la ligne,
  jusqu'à **`\n`** ou **`EOF`** (voir [Reading from stdin](https://github.com/HE-Arc/ARGOS#reading-from-stdin)).
- L'affichage se termine par un retour à la ligne.
