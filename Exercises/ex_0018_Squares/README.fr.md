<!-- Generated at publication from metadata.json — do not edit by hand -->

# 0018 — Squares

**Langage :** C

**Difficulté :** 🟢 facile

**Compétences testées :**
- boucle for
- fonctions (paramètres par valeur)

## Tâche

Implémentez les deux fonctions qui calculent le carré des nombres inférieurs
ou égaux à une valeur donnée :

1. **`ex_0018_Square`** reçoit une valeur entière et retourne son carré.
2. **`ex_0018_Squares`** reçoit une valeur entière qui doit être comprise
   entre 1 et 1000, bornes incluses. En cas de valeur hors bornes, la
   fonction n'affiche rien et retourne **`false`**. Dans le cas contraire,
   elle affiche les carrés des entiers de 1 à la valeur, dans l'ordre
   croissant, et retourne **`true`**.

## Signature

- **`ex_0018_Square`** prend un paramètre de type **`int`** et retourne un
  **`int`**.
- **`ex_0018_Squares`** prend un paramètre de type **`int`** et retourne un
  **`bool`**.

## Sortie attendue

Un appel à **`ex_0018_Squares(5)`** doit afficher :

```
1 4 9 16 25 
```

## Contraintes

- Terminez l'affichage de chaque carré par un espace.
- L'affichage se termine par un retour à la ligne.
