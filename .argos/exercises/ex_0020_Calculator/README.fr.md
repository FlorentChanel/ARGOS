<!-- Generated at publication from metadata.json — do not edit by hand -->

# 0020 — Calculator

**Langage :** C

**Difficulté :** 🟡 moyen

**Compétences testées :**
- conditions (if / switch)
- fonctions (paramètres par valeur)

## Tâche

Implémentez **`ex_0020_Calculator`** pour qu'elle effectue des opérations
mathématiques simples : **`+`**, **`-`**, **`*`**, **`/`**. La fonction
retourne le résultat de l'opération indiquée par l'opérateur, appliquée à
ses deux opérandes.

On tiendra compte des risques de division par zéro : dans ce cas, la
fonction retourne zéro. La fonction retourne aussi zéro lorsque le
caractère n'est pas l'un des quatre opérateurs.

## Signature

**`ex_0020_Calculator`** prend trois paramètres, dans cet ordre : deux
opérandes **`double`** et un opérateur **`char`**. Elle retourne un
**`double`**.

## Exemples

| Appel                                   | valeur retournée |
|-----------------------------------------|------------------|
| **`ex_0020_Calculator(1, 2, '+')`**     | 3                |
| **`ex_0020_Calculator(1, 2, '-')`**     | -1               |
| **`ex_0020_Calculator(1.1, 9.9, '*')`** | 10.89            |
| **`ex_0020_Calculator(1, 2, '/')`**     | 0.5              |
| **`ex_0020_Calculator(1, 0, '/')`**     | 0                |
| **`ex_0020_Calculator(1, 2, 'z')`**     | 0                |
