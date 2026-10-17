<!-- Generated at publication from metadata.json — do not edit by hand -->

# 0015 — Days In Month

**Langage :** C

**Difficulté :** 🟡 moyen

**Compétences testées :**
- conditions (if / switch)

## Tâche

Complétez **`ex_0015_DaysInMonth`** pour qu'elle demande à l'utilisateur le
numéro d'un mois (1 pour janvier, 2 pour février, ...) et lui affiche le
nombre de jours correspondant (31 jours en janvier, 28 en février, ...).

La ligne de résultat est **`Month <n> has <d> days.`**, où **`<n>`** est le
numéro du mois et **`<d>`** son nombre de jours.

## Signature

```c
void ex_0015_DaysInMonth(void);
```

## Exemples

```
Please enter the number of the month (january=1, ... , december=12): 1
Month 1 has 31 days.
```

```
Please enter the number of the month (january=1, ... , december=12): 12
Month 12 has 31 days.
```

```
Please enter the number of the month (january=1, ... , december=12): 13
Please enter the number of the month (january=1, ... , december=12): 7
Month 7 has 31 days.
```

```
Please enter the number of the month (january=1, ... , december=12): a
Please enter the number of the month (january=1, ... , december=12): b
Please enter the number of the month (january=1, ... , december=12): 0
Please enter the number of the month (january=1, ... , december=12): 8
Month 8 has 31 days.
```

## Contraintes

- Utilisez un **`switch`** sur le mois pour déterminer son nombre de jours.
- Gérez les erreurs de saisie : redemandez tant qu'un mois entre 1 et 12 n'est pas lu.
- Après chaque **`scanf`**, videz **`stdin`** : ignorez le reste de la ligne,
  jusqu'à **`\n`** ou **`EOF`** (voir [Reading from stdin](https://github.com/HE-Arc/ARGOS#reading-from-stdin)).
- L'affichage se termine par un retour à la ligne.
