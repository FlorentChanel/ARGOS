<!-- Generated at publication from metadata.json — do not edit by hand -->

# 0014 — Currency Converter

**Langage :** C

**Difficulté :** 🟡 moyen

**Compétences testées :**
- conditions (if / switch)

## Tâche

Complétez **`ex_0014_CurrencyConverter`** pour qu'elle effectue la
conversion en francs suisses d'une somme donnée en won (W), dollars ($),
yens (Y) ou livres sterling (P). Pour la saisie, utilisez une des
instructions suivantes :

```c
scanf(" %g %c", &amount, &currency); // To store in a float
```

ou

```c
scanf(" %lg %c", &amount, &currency); // To store in a double
```

Pour les taux de change, il faut utiliser les constantes suivantes :

```c
const double WON2CHF = 0.00070;
const double USD2CHF = 0.99;
const double YEN2CHF = 0.0067;
const double POUND2CHF = 1.13;
```

## Signature

```c
void ex_0014_CurrencyConverter(void);
```

## Exemples

```
USAGE: non-negative value [W | $ | Y | P]
Won = W  Dollar = $  Yen = Y  Pound = P
Please enter the amount to convert: 123 W
Swiss francs: 0.086
```

```
USAGE: non-negative value [W | $ | Y | P]
Won = W  Dollar = $  Yen = Y  Pound = P
Please enter the amount to convert: 123 $
Swiss francs: 121.770
```

```
USAGE: non-negative value [W | $ | Y | P]
Won = W  Dollar = $  Yen = Y  Pound = P
Please enter the amount to convert: -123 Y
The input amount is negative!!
USAGE: non-negative value [W | $ | Y | P]
Won = W  Dollar = $  Yen = Y  Pound = P
Please enter the amount to convert: 123 Y
Swiss francs: 0.824
```

```
USAGE: non-negative value [W | $ | Y | P]
Won = W  Dollar = $  Yen = Y  Pound = P
Please enter the amount to convert: 123 L
Unsupported currency!!
USAGE: non-negative value [W | $ | Y | P]
Won = W  Dollar = $  Yen = Y  Pound = P
Please enter the amount to convert: 123 P
Swiss francs: 138.990
```

```
USAGE: non-negative value [W | $ | Y | P]
Won = W  Dollar = $  Yen = Y  Pound = P
Please enter the amount to convert: d W
The input format is not correct!!
USAGE: non-negative value [W | $ | Y | P]
Won = W  Dollar = $  Yen = Y  Pound = P
Please enter the amount to convert: 122 W
Swiss francs: 0.085
```

## Contraintes

- Affichez les réels avec 3 chiffres après la virgule.
- Gérez les erreurs de saisie (mauvais format, devise non supportée,
  montant négatif) : affichez le message fourni correspondant et
  redemandez.
- Si le format de saisie est incorrect, affichez seulement
  **`The input format is not correct!!`**. Sinon, vérifiez d'abord la devise,
  puis le montant : si les deux sont invalides, affichez
  **`Unsupported currency!!`** puis **`The input amount is negative!!`**.
- Seules les lettres majuscules **`W`**, **`Y`** et **`P`** sont supportées :
  les minuscules (**`w`**, **`y`**, **`p`**) sont des devises non supportées.
- Après chaque **`scanf`**, videz **`stdin`** : ignorez le reste de la ligne,
  jusqu'à **`\n`** ou **`EOF`** (voir [Reading from stdin](https://github.com/HE-Arc/ARGOS#reading-from-stdin)).
- L'affichage se termine par un retour à la ligne.
