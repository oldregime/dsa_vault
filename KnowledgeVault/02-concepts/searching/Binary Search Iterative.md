
Binary search is an efficient algorithm for finding a target value within a sorted array. It works by repeatedly dividing the search interval in half until the target is found or the interval is empty.

## Algorithm Overview

1. The array must be sorted first
2. Compare the target value with the middle element
3. If equal, return the index
4. If target is greater, search in the right half
5. If target is smaller, search in the left half
6. Repeat until found or search space is empty

## Implementation in Java

```java
// Simple binary search implementation
public static int binarySearch(int[] arr, int target) {
    int low = 0;
    int high = arr.length - 1;
    
    while (low <= high) {
        int mid = low + (high - low) / 2;  // Prevents integer overflow
        
        if (arr[mid] == target) {
            return mid;  // Target found
        }
        
        if (arr[mid] < target) {
            low = mid + 1;  // Search in right half
        } else {
            high = mid - 1;  // Search in left half
        }
    }
    
    return -1;  // Target not found
}
```

## Time Complexity

- **Best Case**: O(1) - Target is the middle element
- **Average Case**: O(log n) - With each comparison, we eliminate half of the remaining elements
- **Worst Case**: O(log n) - We need to divide the array log n times

## Space Complexity

- **Iterative Implementation**: O(1) - Constant space
- **Recursive Implementation**: O(log n) - Due to call stack

## Important Notes

1. **Array must be sorted first** - Binary search only works on sorted arrays
2. **Mid calculation**: Use `mid = low + (high - low) / 2` instead of `(low + high) / 2` to avoid integer overflow
3. **Arrays.toString(arr)** - Useful method to convert arrays to strings for printing
4. **Condition is `low <= high`** - The equal sign is important to handle single-element arrays
5. **Updating bounds** - Always exclude the middle element after checking it (`low = mid + 1` or `high = mid - 1`)

## Advantages

- Very efficient for large datasets - Much faster than linear search
- Logarithmic time complexity means even with billions of elements, it takes few comparisons

## Disadvantages

- Only works on sorted arrays
- Less efficient than linear search for small arrays
- Not suitable for data structures that don't allow random access (like linked lists)

## Applications

- Searching in large sorted datasets
- Dictionary lookup
- Finding a range of values
- Can be extended to solve various problems like finding the first or last occurrence of an element