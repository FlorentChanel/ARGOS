<!-- Generated at publication from metadata.json — do not edit by hand -->

# 0182 — String Via Ptr

**Langage :** C

**Difficulté :** 🟢 facile

**Compétences testées :**
- pointeurs / déréférencement

## Tâche

Implémentez **`ex_0182_StringViaPtr`** pour qu'elle retourne le nombre de
caractères de la chaîne passée en paramètre, en la parcourant avec un pointeur.

## Signature

**`ex_0182_StringViaPtr`** prend un paramètre : **`text`** de type pointeur sur
un **`char`** constant (une chaîne terminée par un caractère nul). Elle retourne
un **`int`** : le nombre de caractères de **`text`**, le **`'\0'`** final non
compris.

## Exemples

```c
ex_0182_StringViaPtr("hello")
```

retourne **`5`**.

```c
ex_0182_StringViaPtr("")
```

retourne **`0`**.

```c
ex_0182_StringViaPtr("a b c")
```

retourne **`5`**.

```c
ex_0182_StringViaPtr("C\n")
```

retourne **`2`**.

## Contraintes

- N'utilisez ni **`strlen`** ni aucune autre fonction de **`string.h`**.
- N'utilisez pas l'opérateur **`[]`**.
