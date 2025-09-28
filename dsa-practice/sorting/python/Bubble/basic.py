def bubble_sort(arr):
    n = len(arr)
    # Outer loop for passes through the array
    for i in range(n):
        # Inner loop for comparisons and swaps in each pass
        # The last 'i' elements are already in place, so we don't need to check them
        for j in range(0, n - i - 1):
            # Compare adjacent elements
            if arr[j] > arr[j + 1]:
                # Swap if they are in the wrong order
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# Example usage:
my_list = [64, 34, 25, 12, 22, 11, 90]
sorted_list = bubble_sort(my_list)
print(f"Sorted array: {sorted_list}")