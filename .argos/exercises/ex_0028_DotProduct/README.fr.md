<!-- Generated at publication from metadata.json — do not edit by hand -->

# 0028 — Dot Product

**Langage :** C

**Difficulté :** 🟢 facile

**Compétences testées :**
- tableaux 1D

## Tâche

Implémentez **`ex_0028_DotProduct`** pour qu'elle calcule le produit
scalaire de 2 vecteurs d'entiers $\vec{u}$ et $\vec{v}$. Les vecteurs
sont passés en paramètres sous forme de tableaux d'entiers, avec leur
taille, dans cet ordre.

Le produit scalaire est la somme des produits des éléments de même indice,
pour les **`n`** éléments :

$$\vec{u} \cdot \vec{v} = u_0 v_0 + u_1 v_1 + \dots + u_{n-1} v_{n-1}$$

## Signature

**`ex_0028_DotProduct`** prend deux tableaux d'entiers (**`int`**), puis leur
taille **`n`** (**`int`**), dans cet ordre, et renvoie leur produit scalaire
(**`int`**).

## Exemples

Avec les tableaux suivants :

```c
int u[] = {3, 2, -4};
int v[] = {2, -3, 5};
```

**`ex_0028_DotProduct(u, v, 3)`** renvoie **`-20`**
($3 \times 2 + 2 \times (-3) + (-4) \times 5 = -20$).

## Contraintes

- **`n`** vaut au moins 1 et les deux tableaux ont **`n`** éléments.
- Chaque produit $u_i v_i$, chaque somme partielle et le produit scalaire
  tiennent dans un **`int`**.
