<!-- Generated at publication from metadata.json — do not edit by hand -->

# 0009 — Circle

**Langage :** C

**Difficulté :** 🟡 moyen

**Compétences testées :**
- entrées-sorties formatées

## Tâche

Complétez **`ex_0009_Circle`** pour qu'elle calcule la surface d'un cercle
lorsqu'on introduit la valeur du rayon. Le rayon est un nombre réel
(**`double`**) ; la saisie est toujours une valeur valide et non négative.

Avant la surface, la fonction affiche pi (le **`M_PI`** fourni) avec
6 chiffres après le point. La surface est affichée avec 2 chiffres
après le point.

## Signature

```c
void ex_0009_Circle(void);
```

## Sortie attendue

La session console se présente ainsi (**`1`** est saisi par l'utilisateur) :

```
Circle radius: 1
pi = 3.141593
Circle surface = 3.14
```

> [!WARNING]
> L'affichage se termine par un retour à la ligne.

## Contraintes

- Après chaque **`scanf`**, videz **`stdin`** : ignorez le reste de la ligne,
  jusqu'à **`\n`** ou **`EOF`** (voir [Reading from stdin](https://github.com/HE-Arc/ARGOS#reading-from-stdin)).
