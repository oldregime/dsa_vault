# Arrays Overview

## 📋 Overview
Arrays are fundamental data structures that store elements of the same type in contiguous memory locations. Each element can be accessed directly using its index, making arrays one of the most efficient data structures for random access.

## 🎯 Key Points
- **Contiguous Memory**: Elements stored in adjacent memory locations
- **Index-based Access**: O(1) time complexity for accessing any element
- **Fixed Size**: Static arrays have predetermined size at compile time
- **Same Data Type**: All elements must be of the same type
- **Zero-indexed**: Most languages use 0-based indexing

## 💡 Implementation

### Java
```java
// Static array declaration
int[] arr = new int[5];           // Creates array of size 5
int[] nums = {1, 2, 3, 4, 5};     // Array with initial values

// Dynamic array (ArrayList)
ArrayList<Integer> list = new ArrayList<>();
list.add(10);
list.add(20);
```

### Python
```python
# Lists in Python (dynamic arrays)
arr = [1, 2, 3, 4, 5]             # List with initial values
empty_list = []                    # Empty list

# Array module (more memory efficient)
import array
nums = array.array('i', [1, 2, 3, 4, 5])  # 'i' for integers
```

## ⏰ Time Complexity
- **Access by index**: O(1)
- **Search (unsorted)**: O(n)
- **Search (sorted)**: O(log n) with binary search
- **Insert at end**: O(1) amortized (dynamic arrays)
- **Insert at beginning/middle**: O(n)
- **Delete**: O(n) in worst case

## 💾 Space Complexity
- **Storage**: O(n) where n is the number of elements
- **Additional space for operations**: Usually O(1)

## 🔗 Related Concepts
- [[Two Pointers Technique]]
- [[Sliding Window]]
- [[Binary Search]]
- [[Dynamic Programming]]

## 📚 Resources
- [GeeksforGeeks - Arrays](https://www.geeksforgeeks.org/array-data-structure/)
- [LeetCode Array Problems](https://leetcode.com/tag/array/)

## 🎴 Anki Cards
**Q:** What is the time complexity for accessing an element by index in an array?
**A:** O(1) - Constant time, because memory address = base_address + (index × element_size)

**Q:** Why are arrays efficient for random access?
**A:** Because elements are stored in contiguous memory, we can calculate any element's address directly using its index.

**Q:** What's the difference between static and dynamic arrays?
**A:** Static arrays have fixed size at compile time, dynamic arrays can grow/shrink at runtime.

---
Tags: #concept/arrays #data-structure #fundamental
Created: 2025-09-23
