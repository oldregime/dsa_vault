# 🦴 Two Pointer Skeletons (Revision)

### 1. Type A: Opposite Ends (Meet in the Middle)
**Use for:** Sorted arrays, Palindromes, Reversing.
```python
def opposite_ends(arr):
    left, right = 0, len(arr) - 1
    while left < right:
        # 1. Check condition
        if arr[left] + arr[right] == target:
            return [left, right]
        
        # 2. Move based on logic
        if arr[left] + arr[right] < target:
            left += 1
        else:
            right -= 1
```

### 2. Type B: Reader-Writer (Same Direction)
**Use for:** In-place modifications, moving/removing elements while keeping order.
```python
def reader_writer(arr):
    writer = 0
    for reader in range(len(arr)):
        if condition(arr[reader]): # "If this is worth keeping"
            arr[writer], arr[reader] = arr[reader], arr[writer]
            writer += 1
    return writer # New length of valid elements
```

### 3. Type D: Fast & Slow (Tortoise & Hare)
**Use for:** Cycles in Linked Lists or arrays, finding the middle.
```python
def fast_slow(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next       # 1 step
        fast = fast.next.next  # 2 steps
        if slow == fast:
            return True # Cycle detected
    return False
```
