<!-- Generated at publication from metadata.json — do not edit by hand -->

# 0022 — Invert

**Langage :** C

**Difficulté :** 🟡 moyen

**Compétences testées :**
- boucle while
- fonctions (paramètres par valeur)

## Tâche

Implémentez **`ex_0022_Invert`** pour qu'elle inverse les chiffres composant
un nombre entier. Toute entrée négative est une erreur : la fonction retourne
alors **`-1`**.

## Signature

**`ex_0022_Invert`** prend un paramètre : le nombre **`int`** **`n`** à
inverser. Elle retourne un **`int`**.

## Exemples

| Appel                        | valeur retournée |
|------------------------------|------------------|
| **`ex_0022_Invert(1234)`**   | 4321             |
| **`ex_0022_Invert(1200)`**   | 21               |
| **`ex_0022_Invert(0)`**      | 0                |
| **`ex_0022_Invert(-12)`**    | -1               |

## Contraintes

- Lorsque **`n`** n'est pas négatif, sa valeur inversée tient dans un
  **`int`** (les entrées comme **`1000000009`** sont exclues).
