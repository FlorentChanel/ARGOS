<!-- Generated at publication from metadata.json — do not edit by hand -->

# 0189 — Pointer Compare

**Langage :** C

**Difficulté :** 🟡 moyen

**Compétences testées :**
- pointeurs / déréférencement

## Tâche

Implémentez **`ex_0189_PointerCompare`** pour qu'elle compare, élément par
élément, deux zones d'entiers dont les adresses sont passées en paramètres.

## Signature

**`ex_0189_PointerCompare`** prend trois paramètres : **`first`** et
**`second`**, deux pointeurs sur le premier élément d'une zone de **`int`**
(non modifiée), et **`size`** de type **`int`**, le nombre d'éléments à
comparer. Elle retourne un **`int`** :

- **`0`** si les **`size`** éléments des deux zones sont égaux ;
- **`-1`** si, à la première position où elles diffèrent, l'élément de
  **`first`** est plus petit que celui de **`second`** ;
- **`1`** si, à cette position, l'élément de **`first`** est plus grand.

## Exemples

```c
int a[] = {1, 2, 3, 4};
int b[] = {1, 2, 3, 4};
int result = ex_0189_PointerCompare(a, b, 4);
```

**`result`** vaut **`0`**.

```c
int a[] = {1, 2, 3, 4};
int b[] = {1, 2, 5, 0};
int result = ex_0189_PointerCompare(a, b, 4);
```

**`result`** vaut **`-1`**.

```c
int a[] = {7, -2, 9};
int b[] = {7, -8, 100};
int result = ex_0189_PointerCompare(a, b, 3);
```

**`result`** vaut **`1`**.

```c
int a[] = {5, 6, 7};
int b[] = {5, 6, 8};
int result = ex_0189_PointerCompare(a, b, 2);
```

**`result`** vaut **`0`**.

```c
int data[] = {3, 4, 3, 4, 9};
int result = ex_0189_PointerCompare(data, data + 2, 3);
```

**`result`** vaut **`-1`**.

```c
int a[] = {1};
int b[] = {2};
int result = ex_0189_PointerCompare(a, b, 0);
```

**`result`** vaut **`0`**.
