## 📋 Overview
- divide-and-conquer approach
- choosing one element as a pivot element and partitioning the array around it
	- Left side = all the elements that are less than the pivot element
	- Right side = all elements greater than the pivot

1. ***Choose a Pivot:** Select an element from the array as the pivot. The choice of pivot can vary (e.g., first element, last element, random element, or median).
2. **Partition the Array:** Re arrange the array around the pivot. After partitioning, all elements smaller than the pivot will be on its left, and all elements greater than the pivot will be on its right. The pivot is then in its correct position, and we obtain the index of the pivot.
3. ***Recursively Call:** Recursively apply the same process to the two partitioned sub-arrays (left and right of the pivot).
4. **Base Case:** The recursion stops when there is only one element left in the sub-array, as a single element is already sorted.

![[Pasted image 20250928170557.png]]

## 🎯 Key Points
- Point 1
- Point 2
- Point 3

## 💡 Implementation
### Java
```java
// Java implementation
```

### Python
```python
# Python implementation
```

## ⏰ Time Complexity
- Operation: O(?)

## 💾 Space Complexity
- Storage: O(?)

## 🔗 Related Concepts
- [[Related Concept 1]]
- [[Related Concept 2]]

## 📚 Resources
- [External Link](url)

## 🎴 Anki Cards
Q: What is {{concept}}?
A: {{answer}}

---
Tags: #concept/{{category}} #language/java #language/python
Created: {{date}}
