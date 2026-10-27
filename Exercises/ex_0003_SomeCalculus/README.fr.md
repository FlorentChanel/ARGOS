<!-- Generated at publication from metadata.json — do not edit by hand -->

# 0003 — Some Calculus

**Langage :** C

**Difficulté :** 🟢 facile

**Compétences testées :**
- opérateurs arithmétiques
- variables et types

## Tâche

Complétez **`ex_0003_SomeCalculus`** pour qu'elle calcule les cinq valeurs
suivantes à partir des deux nombres réels **`a`** et **`b`** :

1. $a^b$ (**`a`** élevé à la puissance **`b`**)
2. l'hypoténuse d'un triangle rectangle dont les côtés sont **`a`** et **`b`** : $\sqrt{a^2 + b^2}$
3. la tangente de **`a`**, où **`a`** est un angle **en degrés**
4. $a / b$ arrondi vers le bas à l'entier
5. $a / b$ arrondi vers le bas à 3 décimales

Les appels **`printf`** sont déjà fournis dans le squelette : pour chaque étape,
calculez seulement la valeur et stockez-la dans **`res`**.

## Signature

```c
void ex_0003_SomeCalculus(double a, double b);
```

## Sortie attendue

Pour **`a = 4`** et **`b = 7`**, la fonction affiche :

```
 a) 4.000000 power 7.000000 = 16384 

 b) The hypotenuse of the right triangle is 8.062258 

 c) The tangent of A is 0.069927 

 d) The rounded down value of A/B is 0.000000 

 e) The rounded down value of A/B with 3 decimals is 0.571000 
```

La sortie commence par une ligne vide (avant la partie a)) et se termine par une
ligne vide (après la partie e)).

## Contraintes

- Les entrées sont toujours valides : **`b`** est non nul, $a^b$ est défini
  (**`a`** n'est pas négatif lorsque **`b`** n'est pas un entier), et **`a`** n'est
  pas un multiple impair de 90 degrés.
- Utilisez les fonctions de la bibliothèque mathématique standard (**`math.h`**
  est déjà inclus) : **`pow`**, **`sqrt`**, **`sin`**, **`cos`**, **`floor`**.
- Calculez la tangente en n'utilisant que **`sin`** et **`cos`**.
- Ne modifiez ni les appels **`printf`** fournis, ni la signature de la fonction.

> [!WARNING]
> Les fonctions trigonométriques de **`math.h`** travaillent en **radians**,
> alors que **`a`** est donné en **degrés**.
