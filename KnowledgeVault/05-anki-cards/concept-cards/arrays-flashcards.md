# 🎴 Arrays Concept Flashcards

## Basic Array Concepts

### Card 1: Array Definition
**Q:** What is an array in data structures?
**A:** A collection of elements stored in contiguous memory locations, where each element can be accessed using an index.

### Card 2: Array Access Time
**Q:** What is the time complexity for accessing an element by index in an array?
**A:** O(1) - Constant time, because we can calculate the memory address directly using the formula: base_address + (index × element_size)

### Card 3: Array Search Time
**Q:** What is the time complexity for searching an element in an unsorted array?
**A:** O(n) - Linear time, because in the worst case we might need to check every element

### Card 4: Array Insertion
**Q:** What is the time complexity for inserting an element at the beginning of an array?
**A:** O(n) - Linear time, because we need to shift all existing elements to the right

### Card 5: Dynamic vs Static Arrays
**Q:** What is the difference between static and dynamic arrays?
**A:** Static arrays have fixed size at compile time, dynamic arrays (like ArrayList in Java) can grow/shrink at runtime

## Array Techniques

### Card 6: Two Pointers Technique
**Q:** When do you use the two pointers technique?
**A:** When you need to find pairs, reverse array, or search in sorted array. Use one pointer at start, one at end, move based on condition.

### Card 7: Sliding Window
**Q:** What is the sliding window technique and when to use it?
**A:** Maintain a window of elements and slide it across the array. Used for subarray problems like "find max sum of k consecutive elements"

### Card 8: Prefix Sum
**Q:** What is prefix sum and its advantage?
**A:** Array where each element is sum of all previous elements. Allows O(1) range sum queries after O(n) preprocessing.

## Common Problems

### Card 9: Two Sum Pattern
**Q:** What's the optimal approach for Two Sum problem?
**A:** Use HashMap to store (value → index). For each element, check if (target - current) exists in map. Time: O(n), Space: O(n)

### Card 10: Array Rotation
**Q:** How to rotate array by k positions to the right in O(1) space?
**A:** 
1. Reverse entire array
2. Reverse first k elements  
3. Reverse remaining elements

### Card 11: Remove Duplicates
**Q:** How to remove duplicates from sorted array in-place?
**A:** Use two pointers: slow pointer for unique elements position, fast pointer to scan array. Time: O(n), Space: O(1)

---
*Export these to Anki for spaced repetition practice*
