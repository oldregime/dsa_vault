
### 1. Declaration Only

```java
int[] arr1;      // Preferred style
int arr2[];      // Also valid, but less common
```

### 2. Declaration and Allocation

```java
int[] arr = new int[5];      // Array of 5 integers, default values 0
char[] chars = new char[3];  // Array of 3 chars, default values '\u0000'
float[] floats = new float[4]; // Array of 4 floats, default values 0.0f
```

### 3. Declaration, Allocation, and Initialization

```java
int[] arr = {1, 2, 3, 4, 5};           // Array with values
char[] chars = {'a', 'b', 'c'};        // Array with values
float[] floats = {1.2f, 3.4f, 5.6f};   // Array with values
String[] words = {"Java", "Array"};    // Array of Strings
```

## 4 Type
![[Untitled 1.jpg]]
### 4. Multidimensional Arrays

```java
int[][] matrix = new int[3][4];        // 2D array, 3 rows, 4 columns
int[][] mat = { {1,2}, {3,4}, {5,6} }; // 2D array with values
```

### 5. Invalid Declarations

```java
// int[5] arr = new int[5]; // ❌ Invalid syntax
```
You cannot specify the size in the declaration part, only in the allocation.

---

**Summary Table:**

| Syntax                        | Description                        |
|-------------------------------|------------------------------------|
| `int[] arr;`                  | Declaration only                   |
| `int[] arr = new int[5];`     | Declaration + allocation           |
| `int[] arr = {1,2,3};`        | Declaration + initialization       |
| `int[][] arr = new int[2][3];`| 2D array declaration + allocation  |

