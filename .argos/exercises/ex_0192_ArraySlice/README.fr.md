<!-- Generated at publication from metadata.json — do not edit by hand -->

# 0192 — Array Slice

**Langage :** C

**Difficulté :** 🟡 moyen

**Compétences testées :**
- arithmétique des pointeurs

## Tâche

Implémentez **`ex_0192_ArraySlice`** pour qu'elle copie une tranche d'un
tableau d'entiers dans un second tableau : les éléments de l'indice
**`start`** inclus à l'indice **`end`** exclu, dans le même ordre. Elle
retourne le nombre d'éléments copiés. Le tableau source n'est pas modifié.

Si les bornes sont invalides (**`start`** négatif, **`end`** plus grand que
**`size`**, ou **`start`** plus grand que **`end`**), rien n'est copié et la
fonction retourne **`-1`**.

## Signature

**`ex_0192_ArraySlice`** prend cinq paramètres : **`source`** de type pointeur
sur un **`int`** constant (le premier élément du tableau à découper),
**`size`** de type **`int`** (le nombre d'éléments de **`source`**),
**`start`** et **`end`** de type **`int`** (les bornes de la tranche), et
**`destination`** de type pointeur sur un **`int`** (le premier élément du
tableau qui reçoit la tranche). Elle retourne un **`int`** : le nombre
d'éléments copiés, ou **`-1`**.

## Exemples

```c
int source[] = {10, 20, 30, 40, 50, 60};
int destination[6];
int count = ex_0192_ArraySlice(source, 6, 1, 4, destination);
```

**`count`** vaut **`3`** et les trois premiers éléments de **`destination`**
sont **`{20, 30, 40}`**. **`source`** vaut toujours
**`{10, 20, 30, 40, 50, 60}`**.

```c
int source[] = {-5, 7, 0, 3};
int destination[4];
int count = ex_0192_ArraySlice(source, 4, 0, 4, destination);
```

**`count`** vaut **`4`** et **`destination`** vaut **`{-5, 7, 0, 3}`**.

```c
int source[] = {1, 2, 3, 4, 5};
int destination[5];
int count = ex_0192_ArraySlice(source, 5, 4, 5, destination);
```

**`count`** vaut **`1`** et le premier élément de **`destination`** vaut
**`5`**.

```c
int source[] = {1, 2, 3};
int destination[3] = {9, 9, 9};
int count = ex_0192_ArraySlice(source, 3, 2, 2, destination);
```

**`count`** vaut **`0`** et **`destination`** vaut toujours **`{9, 9, 9}`**.

```c
int source[] = {1, 2, 3};
int destination[3] = {9, 9, 9};
int count = ex_0192_ArraySlice(source, 3, 1, 4, destination);
```

**`count`** vaut **`-1`** et **`destination`** vaut toujours **`{9, 9, 9}`**.
Il en va de même pour **`start`** égal à **`-1`**, ou pour **`start`** égal à
**`2`** avec **`end`** égal à **`1`**.

## Contraintes

- **`size`** vaut au moins **`1`**.
- **`destination`** contient au moins **`size`** éléments et ne chevauche pas
  **`source`**.
- Aucun élément de **`destination`** n'est modifié au-delà de la tranche
  copiée.
