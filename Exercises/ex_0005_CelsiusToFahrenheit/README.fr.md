<!-- Generated at publication from metadata.json — do not edit by hand -->

# 0005 — Celsius to Fahrenheit

**Langage :** C

**Difficulté :** 🟢 facile

**Compétences testées :**
- opérateurs arithmétiques

## Tâche

Complétez **`ex_0005_CelsiusToFahrenheit`** pour qu'elle convertisse la
température **`temperatureC`** (degrés Celsius) en Fahrenheit et retourne le
résultat. La conversion est $F = 1.8 \times C + 32$.

## Signature

```c
double ex_0005_CelsiusToFahrenheit(double temperatureC);
```

## Exemples

| **`temperatureC`** | valeur retournée |
|--------------------|------------------|
| 0                  | 32               |
| 100                | 212              |
| -40                | -40              |
| 37.5               | 99.5             |

## Contraintes

- Toute température réelle est valide, y compris négative.
- Utilisez **`double`** pour le calcul.
