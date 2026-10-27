<!-- Generated at publication from metadata.json — do not edit by hand -->

# 0017 — Factorial

**Langage :** C

**Difficulté :** 🟢 facile

**Compétences testées :**
- boucle for

## Tâche

Complétez **`ex_0017_Factorial`** pour qu'elle lise un entier non négatif $N$,
puis calcule et affiche sa factorielle $N!$ telle que :

$$N! = 1 \times 2 \times 3 \times \dots \times (N-1) \times N$$

et

$$0! = 1$$

## Signature

```c
void ex_0017_Factorial(void);
```

## Exemples

```
Please enter a non-negative integer N: 6
6! = 720
```

```
Please enter a non-negative integer N: 0
0! = 1
```

```
Please enter a non-negative integer N: -1
Please enter a non-negative integer N: a
Please enter a non-negative integer N: 6
6! = 720
```

## Contraintes

- Calculez $N!$ avec une boucle (pas de récursivité).
- Gérez les erreurs de saisie : redemandez tant qu'un entier non négatif n'est pas lu.
- Le résultat affiché doit être exact pour tout $N$ de **`0`** à **`20`**.
- Après chaque **`scanf`**, videz **`stdin`** : ignorez le reste de la ligne,
  jusqu'à **`\n`** ou **`EOF`** (voir [Reading from stdin](https://github.com/HE-Arc/ARGOS#reading-from-stdin)).
- L'affichage se termine par un retour à la ligne.
