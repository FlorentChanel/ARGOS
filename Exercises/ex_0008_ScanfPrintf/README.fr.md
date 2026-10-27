<!-- Generated at publication from metadata.json — do not edit by hand -->

# 0008 — Scanf Printf

**Langage :** C

**Difficulté :** 🟢 facile

**Compétences testées :**
- entrées-sorties formatées

## Tâche

Complétez **`ex_0008_ScanfPrintf`** pour qu'elle demande 3 lettres à
l'utilisateur et affiche leurs codes ASCII. La saisie contient toujours
3 lettres ; elles peuvent être tapées sans séparateur (**`abc`**), séparées
par des espaces (**`a b c`**) ou séparées par des retours à la ligne.

## Signature

```c
void ex_0008_ScanfPrintf(void);
```

## Sortie attendue

La session console se présente ainsi (**`a b c`** est saisi par
l'utilisateur) :

```


Please enter 3 letters:
a b c

Here are the corresponding ASCII codes:
a--------->97
b--------->98
c--------->99
```

La fonction affiche exactement :

1. **`"\n\nPlease enter 3 letters:\n"`** avant de lire les lettres (deux
   retours à la ligne, puis l'invite, qui se termine par un retour à la
   ligne) ;
2. **`"\nHere are the corresponding ASCII codes:\n"`** après les avoir
   lues : la ligne vide au-dessus de cette ligne est affichée par la
   fonction, ce n'est pas l'écho de la touche Entrée de l'utilisateur ;
3. une ligne par lettre, dans l'ordre de saisie : la lettre,
   **`--------->`**, puis son code ASCII, suivi d'un retour à la ligne.

> [!WARNING]
> L'affichage commence par 2 retours à la ligne et se termine par un
> retour à la ligne.

## Contraintes

> [!WARNING]
> Après avoir lu la troisième lettre (avec **`scanf`**), vous **devez**
> vider **`stdin`** (jusqu'à **`\n`** ou **`EOF`**).
> Voir [Reading from stdin](https://github.com/HE-Arc/ARGOS#reading-from-stdin).
