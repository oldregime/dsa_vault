# Bubble Sort

## 📋 Overview
Bubble Sort is a simple comparison-based sorting algorithm that repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order. The pass through the list is repeated until the list is sorted.

**Why "Bubble" Sort?** 
The algorithm is named "Bubble Sort" because smaller elements "bubble up" to the top of the list and larger elements "sink" to the bottom with each pass, similar to bubbles rising in a liquid.

### Key Characteristics:
- **Simple** but **inefficient** for large datasets
- **Stable** sorting algorithm (maintains relative order of equal elements)
- **In-place** sorting (requires only O(1) extra memory)
- **Adaptive** (can be optimized for nearly sorted arrays)

## 🔄 How It Works

### Algorithm Steps:
1. Start with the first element in the array
2. Compare each pair of adjacent elements
3. If they are in wrong order, swap them
4. Continue until the end of array (one pass complete)
5. Repeat passes until no swaps are needed

### Example Walk through:
```
Initial: [64, 34, 25, 12, 22, 11, 90]

Pass 1: [34, 25, 12, 22, 11, 64, 90] (90 in position)
Pass 2: [25, 12, 22, 11, 34, 64, 90] (64 in position)  
Pass 3: [12, 22, 11, 25, 34, 64, 90] (34 in position)
Pass 4: [12, 11, 22, 25, 34, 64, 90] (25 in position)
Pass 5: [11, 12, 22, 25, 34, 64, 90] (22 in position)
Pass 6: [11, 12, 22, 25, 34, 64, 90] (No swaps - sorted!)
```

## 💡 Implementation

### Python
```python
def bubble_sort(arr):
    n = len(arr)
    # Outer loop for passes through the array
    for i in range(n):
        # Flag to optimize - if no swaps occur, array is sorted
        swapped = False
        
        # Inner loop for comparisons and swaps in each pass
        # The last 'i' elements are already in place
        for j in range(0, n - i - 1):
            # Compare adjacent elements
            if arr[j] > arr[j + 1]:
                # Swap if they are in the wrong order
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        
        # If no swapping occurred, array is sorted
        if not swapped:
            break
            
    return arr
```

### Java
```java
public class BubbleSort {
    static void bubbleSort(int arr[], int n) {
        boolean swapped;
        
        for (int i = 0; i < n - 1; i++) {
            swapped = false;
            
            // Last i elements are already in place
            for (int j = 0; j < n - i - 1; j++) {
                if (arr[j] > arr[j + 1]) {
                    // Swap elements
                    int temp = arr[j];
                    arr[j] = arr[j + 1];
                    arr[j + 1] = temp;
                    swapped = true;
                }
            }
            
            // If no swapping occurred, array is sorted
            if (!swapped) break;
        }
    }
}
```

## ⏰ Time Complexity
- **Best Case**: O(n) - when array is already sorted (with optimization)
- **Average Case**: O(n²) - random order
- **Worst Case**: O(n²) - when array is reverse sorted

### Pass Analysis:
- **Number of passes**: n-1 (worst case)
- **Comparisons per pass**: decreases from (n-1) to 1
- **Total comparisons**: n(n-1)/2 = O(n²)

## 💾 Space Complexity
- **Space**: O(1) - only uses a constant amount of extra space for temporary variables
- **In-place sorting**: Yes, sorts the array without requiring additional storage

## ✅ Advantages & Disadvantages

### Advantages:
- Simple to understand and implement
- No additional memory space needed
- Stable sorting algorithm
- Can detect if list is already sorted (optimized version)
- Works well for small datasets

### Disadvantages:
- Poor time complexity O(n²) for large datasets
- More swaps compared to other O(n²) algorithms like Selection Sort
- Generally performs worse than insertion sort

## 🔄 Optimization Techniques

### 1. Early Termination
If no swaps occur during a pass, the array is sorted:
```python
if not swapped:
    break  # Array is sorted, exit early
```

### 2. Cocktail Shaker Sort (Bidirectional Bubble Sort)
Alternates between forward and backward passes to move both large and small elements efficiently.

## 🆚 Comparison with Other Sorts

| Algorithm | Best | Average | Worst | Space | Stable |
|-----------|------|---------|-------|-------|--------|
| Bubble Sort | O(n) | O(n²) | O(n²) | O(1) | Yes |
| Selection Sort | O(n²) | O(n²) | O(n²) | O(1) | No |
| Insertion Sort | O(n) | O(n²) | O(n²) | O(1) | Yes |
| Merge Sort | O(n log n) | O(n log n) | O(n log n) | O(n) | Yes |

## 🎯 When to Use Bubble Sort
- **Educational purposes** - learning sorting concepts
- **Small datasets** (< 50 elements)
- **Nearly sorted data** (with optimization)
- **When simplicity is more important than efficiency**
- **Memory is extremely limited** (embedded systems)

## 🔗 Related Concepts
- [[Selection Sort]] - Similar O(n²) but fewer swaps
- [[Insertion Sort]] - Better performance for small/nearly sorted arrays
- [[Cocktail Shaker Sort]] - Optimized bidirectional bubble sort
- [[Sorting Algorithms Overview]]

## 📚 Resources
- [GeeksforGeeks - Bubble Sort](https://www.geeksforgeeks.org/bubble-sort/)
- [Visualgo - Sorting Visualizer](https://visualgo.net/en/sorting)
- [Algorithm Visualizer](https://algorithm-visualizer.org/)

## 🎴 Anki Cards

**Q:** What is the time complexity of Bubble Sort in worst case?
**A:** O(n²) - when array is sorted in reverse order

**Q:** Why is Bubble Sort called "Bubble" Sort?
**A:** Because smaller elements "bubble up" to the top while larger elements "sink" to the bottom, like bubbles in liquid

**Q:** What optimization can make Bubble Sort run in O(n) for best case?
**A:** Adding a flag to check if any swaps occurred; if no swaps in a pass, the array is sorted

**Q:** Is Bubble Sort stable?
**A:** Yes, it maintains the relative order of equal elements

---
**Tags:** #algorithm #sorting #basic #O(n²) #stable #inplace #comparison-based
**Created:** September 25, 2025
**Last Modified:** September
