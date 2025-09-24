Linear search, also known as sequential search, is a simple search algorithm that finds the position of a target value within a list by checking each element sequentially until a match is found or the list ends.

## Algorithm

```java
for each element in the list:
    if element equals the target value:
        return the element's position
return -1 (indicating the target value was not found)
```

## Implementation in Java

```java
public static int linearSearch(int[] arr, int key) {
    for (int i = 0; i < arr.length; i++) {
        if (arr[i] == key) {
            return i;
        }
    }
    return -1; // Element not found
}
```

## Time Complexity

- **Best Case**: O(1)
  - Occurs when the target element is found at the first position
  - Only requires one comparison

- **Worst Case**: O(N)
  - Occurs when the target element is at the last position or not in the list at all
  - Requires N comparisons for a list of size N

- **Average Case**: O(N)
  - On average, the algorithm will need to check half the elements before finding the target
  - Still considered O(N) in asymptotic analysis

## Space Complexity

- **O(1)** - Constant space
  - Linear search only uses a fixed amount of extra space regardless of input size
  - No additional data structures are required

## Advantages

- Simple to implement and understand
- Works on unsorted arrays
- No preprocessing required
- Good for small datasets

## Disadvantages

- Inefficient for large datasets
- Much slower than binary search for sorted arrays
- Linear time complexity is not suitable for time-critical applications with large data

## When to Use

- When the list is small
- When the list is unsorted and sorting would be costly
- When simplicity is preferred over efficiency
- When only a few searches are needed
- When the elements are being searched only once

## Variations

- **Sentinel Linear Search**: Places a copy of the target at the end of the array to eliminate the need for boundary checking
- **Improved Linear Search**: Searches from both ends simultaneously

