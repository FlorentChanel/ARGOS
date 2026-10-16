<!-- Generated at publication from metadata.json — do not edit by hand -->

# 0010 — Lowercase Uppercase

**Langage :** C

**Difficulté :** 🟡 moyen

**Compétences testées :**
- conditions (if / switch)

## Tâche

Complétez **`ex_0010_LowercaseUppercase`** pour qu'elle détermine si le
caractère qu'on tape est une minuscule (code ASCII compris entre 97 et 122)
ou une majuscule (code compris entre 65 et 90).

## Signature

```c
void ex_0010_LowercaseUppercase(void);
```

## Exemples

```
Type a letter: u
lowercase
```

```
Type a letter: F
UPPERCASE
```

```
Type a letter: !
The character you entered is not a letter.
```

## Contraintes

- Gérez les erreurs de saisie : redemandez tant qu'aucun caractère n'est lu.
- Après chaque **`scanf`**, videz **`stdin`** : ignorez le reste de la ligne,
  jusqu'à **`\n`** ou **`EOF`** (voir [Reading from stdin](https://github.com/HE-Arc/ARGOS#reading-from-stdin)).
- L'affichage se termine par un retour à la ligne.
