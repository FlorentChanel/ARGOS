<!-- Generated at publication from metadata.json — do not edit by hand -->

# 0006 — Asset Interest Rate

**Langage :** C

**Difficulté :** 🟡 moyen

**Compétences testées :**
- opérateurs arithmétiques
- variables et types

## Tâche

Complétez **`ex_0006_AssetInterestRate`** pour qu'elle calcule la valeur
finale d'un capital initial **`initAssets`**, après application d'un taux
d'intérêt composé annuel **`interestRate`** (en pourcent) pendant
**`years`** années, et la retourne :

$$\text{finalAssets} = \text{initAssets} \times \left(1 + \frac{\text{interestRate}}{100}\right)^{\text{years}}$$

## Signature

```c
double ex_0006_AssetInterestRate(double initAssets, double interestRate, int years);
```

## Exemples

| **`initAssets`** | **`interestRate`** | **`years`**    | valeur retournée |
|------------------|--------------------|----------------|------------------|
| 1000             | 2.5                | 30             | ≈ 2097.57        |
| 1000             | 2.5                | 0              | 1000             |
| 1000             | 0                  | 30             | 1000             |
| 1000             | 2.5                | 1              | 1025             |

## Contraintes

- Utilisez **`pow`** de la bibliothèque mathématique standard (**`math.h`**
  est déjà inclus).
- Les entrées sont toujours valides : **`years`** est positif ou nul et
  **`interestRate`** est strictement supérieur à -100.
