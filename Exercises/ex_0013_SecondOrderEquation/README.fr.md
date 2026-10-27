<!-- Generated at publication from metadata.json — do not edit by hand -->

# 0013 — Second Order Equation

**Langage :** C

**Difficulté :** 🟡 moyen

**Compétences testées :**
- conditions (if / switch)

## Tâche

Complétez **`ex_0013_SecondOrderEquation`** pour qu'elle calcule la ou les
solutions réelles d'une équation du second degré de la forme suivante :

$$ax^2 + bx + c = 0$$

en utilisant la formule suivante :

$$x_{1,2} = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$$

Considérez aussi les cas où l'utilisateur entre :

- une valeur nulle pour **`a`** ;
- des valeurs nulles pour **`a`** et **`b`** ;
- des valeurs nulles pour **`a`**, **`b`** et **`c`**.

Affichez les résultats et les messages nécessaires sur l'écran (les
messages sont fournis dans le squelette).

## Signature

```c
void ex_0013_SecondOrderEquation(void);
```

## Exemples

```
Compute solutions of an equation of the form ax^2 + bx + c = 0
Please enter coefficients a, b, and c: 0 0 0
Any real is solution of this equation.
```

```
Compute solutions of an equation of the form ax^2 + bx + c = 0
Please enter coefficients a, b, and c: 1 1 1
This equation has no real solution.
```

```
Compute solutions of an equation of the form ax^2 + bx + c = 0
Please enter coefficients a, b, and c: 1 1 -2
The real solutions of this equation are: 
x1 = 1.0000
x2 = -2.0000
```

```
Compute solutions of an equation of the form ax^2 + bx + c = 0
Please enter coefficients a, b, and c: 1 -2 1
The double real solution of this equation is: 
x = 1.0000
```

```
Compute solutions of an equation of the form ax^2 + bx + c = 0
Please enter coefficients a, b, and c: 0 2 -4
The solution of this linear equation is: 
x = 2.0000
```

```
Compute solutions of an equation of the form ax^2 + bx + c = 0
Please enter coefficients a, b, and c: 0 0 5
This equation has no solution.
```

```
Compute solutions of an equation of the form ax^2 + bx + c = 0
Please enter coefficients a, b, and c: a 1 2
Compute solutions of an equation of the form ax^2 + bx + c = 0
Please enter coefficients a, b, and c: 1 b -2
Compute solutions of an equation of the form ax^2 + bx + c = 0
Please enter coefficients a, b, and c: 2 -1 -2
The real solutions of this equation are: 
x1 = 1.2808
x2 = -0.7808
```

## Contraintes

- Les coefficients **`a`**, **`b`** et **`c`** sont des réels : une saisie
  décimale comme **`0.5`** est acceptée.
- Affichez les réels avec 4 chiffres après la virgule.
- Une solution nulle peut s'afficher **`0.0000`** ou **`-0.0000`** : les deux
  sont acceptés.
- Gérez les erreurs de saisie : redemandez tant que trois nombres ne sont pas lus.
- Après chaque **`scanf`**, videz **`stdin`** : ignorez le reste de la ligne,
  jusqu'à **`\n`** ou **`EOF`** (voir [Reading from stdin](https://github.com/HE-Arc/ARGOS#reading-from-stdin)).
- L'affichage se termine par un retour à la ligne.
