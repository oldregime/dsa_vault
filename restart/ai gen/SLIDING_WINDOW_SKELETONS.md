# 🦴 Sliding Window Skeletons

### 1. Fixed Size Window
**Use for:** "Find the max sum of a subarray of size K."
```python
def fixed_window(arr, k):
    curr_sum = sum(arr[:k]) # Initialize first window
    max_sum = curr_sum
    
    for i in range(len(arr) - k):
        # 1. Slide the window: subtract left, add right
        curr_sum = curr_sum - arr[i] + arr[i + k]
        max_sum = max(max_sum, curr_sum)
        
    return max_sum
```

### 2. Variable Size Window (Shrinkable)
**Use for:** "Find the shortest subarray with sum >= S."
```python
def variable_window(arr, target):
    left = 0
    curr_sum = 0
    min_len = float('inf')
    
    for right in range(len(arr)):
        # 1. Expand: add right element
        curr_sum += arr[right]
        
        # 2. Shrink: while window is "valid", try to make it smaller
        while curr_sum >= target:
            min_len = min(min_len, right - left + 1)
            curr_sum -= arr[left]
            left += 1
            
    return min_len if min_len != float('inf') else 0
```

### 3. Variable Size Window (Non-Shrinkable)
**Use for:** "Find the longest subarray with at most K distinct elements."
*Crucial difference: The `while` is replaced by an `if` because we only care about the **maximum** size ever reached.*
```python
def non_shrinkable_window(arr, k):
    left = 0
    counts = {}
    
    for right in range(len(arr)):
        # 1. Expand
        counts[arr[right]] = counts.get(arr[right], 0) + 1
        
        # 2. If invalid, just shift the whole window (don't shrink)
        if len(counts) > k:
            counts[arr[left]] -= 1
            if counts[arr[left]] == 0: del counts[arr[left]]
            left += 1
            
    return right - left + 1
```
