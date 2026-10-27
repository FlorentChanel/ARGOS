<!-- Generated at publication from metadata.json — do not edit by hand -->

# 0026 — Array Sum

**Langage :** C

**Difficulté :** 🟢 facile

**Compétences testées :**
- tableaux 1D
- boucle for

## Tâche

Implémentez **`ex_0026_ArraySum`** pour qu'elle :

1. déclare un tableau pouvant contenir 50 entiers maximum
2. demande à l'utilisateur le nombre de valeurs **`n`** à saisir
   (maximum 50)
3. remplisse le tableau avec **`n`** valeurs entrées au clavier
4. affiche les **`n`** premiers éléments du tableau
5. affiche la somme des valeurs saisies se trouvant dans le tableau

## Signature

**`ex_0026_ArraySum`** ne prend aucun paramètre et ne retourne rien (**`void`**).

## Exemples

Dans les exemples, le texte qui suit chaque invite est saisi par l'utilisateur ;
chaque invite se termine par une espace, sans retour à la ligne.

```
Nb values (max.50): a
Nb values (max.50): b
Nb values (max.50): -2
Nb values (max.50): -1
Nb values (max.50): 0
array:

Total sum: 0
```

```
Nb values (max.50): 4
Value 0? -2
Value 1? -1
Value 2? 0
Value 3? 1
array:
-2 -1 0 1
Total sum: -2
```

## Contraintes

- Gérez les erreurs de saisie : **`n`** est valide de 0 à 50, toute autre
  saisie réaffiche l'invite **`Nb values (max.50): `**.
- Une saisie invalide à une invite **`Value i? `** est ignorée et la même invite
  **`Value i? `** est réaffichée.
- Les valeurs du tableau sont affichées sur une ligne, séparées par une espace,
  sans espace finale, puis un retour à la ligne.
- Après chaque **`scanf`**, videz **`stdin`** : ignorez le reste de la ligne,
  jusqu'à **`\n`** ou **`EOF`** (voir [Reading from stdin](https://github.com/HE-Arc/ARGOS#reading-from-stdin)).
- L'affichage se termine par un retour à la ligne.
