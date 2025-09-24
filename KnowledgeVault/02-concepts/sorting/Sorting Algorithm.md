## Definition
- rearrangement of a given array or list of elements according to a comparison operator on the elements

## Why
- Once we get the data sorted, we can get the k-th smallest and k-th largest item in O(1) time.
- Searching any element in a huge data set becomes easy. We can use Binary search method for search if we have sorted data. So, Sorting become important here.

## Sorting Basics

- **In-place Sorting:**
    - Uses constant additional space.
    - Modifies the original array directly.
    - **Examples:** Selection Sort, Bubble Sort, Insertion Sort, Heap Sort.
- **Internal Sorting:**
    - All data resides in main or internal memory.
    - Limited by allocated memory size.
- **External Sorting:**
    - Data does not need to be entirely in memory at once.
    - Used for massive amounts of data.
    - **Example:** Merge Sort.
- **Stable Sorting:**
    - Maintains the relative order of equal elements from the original array in the sorted output.
    - **Examples:** Merge Sort, Insertion Sort, Bubble Sort.
- **Hybrid Sorting:**
       - Combines multiple standard sorting algorithms.
    - Aims to leverage the advantages of different algorithms. 
    - **Example:** IntroSort (uses Insertion Sort and Quick Sort).

## Types of Sorting
![[csyrwqhk.png]]

## Common

[Selection sort](http://www.geeksforgeeks.org/selection-sort/), [Bubble sort](http://www.geeksforgeeks.org/bubble-sort/), [Insertion Sort](http://www.geeksforgeeks.org/insertion-sort/), [Cycle Sort](https://www.geeksforgeeks.org/cycle-sort/), [Merge Sort](http://www.geeksforgeeks.org/merge-sort/), [3-way Merge Sort](https://www.geeksforgeeks.org/3-way-merge-sort/), [Quick sort](http://www.geeksforgeeks.org/quick-sort/), [Heap sort](https://www.geeksforgeeks.org/heap-sort/) and [Counting sort](https://www.geeksforgeeks.org/counting-sort/)