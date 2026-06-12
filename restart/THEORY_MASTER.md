# 🧠 DSA Hard Theory: The "No-Nonsense" Master Guide

> **Goal**: Mastering the 4 fundamental patterns to solve 80% of array/string/list problems.

---

## 1. Two Pointers (The Foundation)

### 🏎️ Mental Model
Think of pointers as **indices** (`i`, `j`) that scan the data. They can move towards each other, or one can "chase" the other.

### 🌓 Sub-Pattern A: Opposite Direction (Meet in the Middle)
*   **Use When**: Array is **sorted** and you need to find a pair, or checking symmetry (Palindromes).
*   **Loop Invariant**: The answer (if it exists) is always between `left` and `right`.
*   **State Transition**:
    *   If `sum < target` $\rightarrow$ `left++` (increases the sum).
    *   If `sum > target` $\rightarrow$ `right--` (decreases the sum).
*   **Stop Condition**: `while left < right`.
*   **Edge Cases**: Even vs. Odd length (for palindromes), duplicates.

### 🏃 Sub-Pattern B: Same Direction (Reader-Writer / Slow-Fast Index)
*   **Use When**: **In-place** modification (Remove Duplicates, Move Zeroes).
*   **Mental Model**: 
    *   `Reader` (Fast): Scans every element.
    *   `Writer` (Slow): Tracks the "boundary" of the valid result.
*   **Loop Invariant**: Everything before `writer` satisfies the condition.
*   **Stop Condition**: `for reader in range(len(arr))`.

---

## 2. Sliding Window (The Subarray Specialist)

### 🪟 Mental Model
A window defined by `[left, right]`. `right` **expands** the window, `left` **shrinks** it when a condition is violated.

### 📏 Fixed Size Window
*   **Use When**: "K consecutive elements", "Length K subarray".
*   **Technique**: Calculate the first window, then subtract `arr[i]` and add `arr[i+k]`.
*   **Complexity**: $O(n)$ time, $O(1)$ space.

### 🎢 Variable Size Window (Shrinkable)
*   **Use When**: "Longest/Shortest subarray where sum/condition X is met."
*   **Logic**:
    1.  `right` pointer always moves forward.
    2.  Check if window is "valid" or "invalid".
    3.  If "invalid" (or "too valid" for shortest), `while` loop shrinks from `left`.
*   **Complexity**: $O(n)$ because each pointer visits each element at most once.

---

## 3. Fast & Slow Pointers (The Cycle Detective)

### 🐢🐇 Mental Model (Tortoise & Hare)
Two pointers moving at different speeds. If there's a cycle, the fast one **must** lap the slow one.

### 🔄 Cycle Detection
*   **Step**: `slow = slow.next`, `fast = fast.next.next`.
*   **The Math**: In a cycle of length $C$, the distance between them increases by 1 each step. They will meet in at most $C$ steps.

### 📍 Middle Finding
*   **Step**: When `fast` reaches the end, `slow` is exactly at the middle.
*   **Edge Case**: 
    *   `while fast and fast.next` $\rightarrow$ `slow` lands on the **second** middle in even lists.

---

## 4. Binary Search (The Search Space Divider)

### 🎯 Mental Model
Repeatedly halving the **Search Space**. It’s not just for sorted arrays; it’s for any **monotonic** function (True, True, ..., False, False).

### 📐 Classical Template
```python
left, right = 0, len(arr) - 1
while left <= right:
    mid = left + (right - left) // 2
    if arr[mid] == target: return mid
    if arr[mid] < target: left = mid + 1
    else: right = mid - 1
```

### 🚀 Advanced: Binary Search on Answer
*   **Use When**: You can't find the answer directly, but you can "check" if a value `X` is possible.
*   **Example**: "Minimum capacity to ship packages within D days."
*   **Search Space**: `min_possible_ans` to `max_possible_ans`.

---

## 🛠️ Implementation Cheat Sheet (Python & Java)

### Two Pointers (Opposite)
| Feature | Python | Java |
| :--- | :--- | :--- |
| Init | `l, r = 0, n-1` | `int l = 0, r = n - 1;` |
| Loop | `while l < r:` | `while (l < r) { ... }` |
| Swap | `a[l], a[r] = a[r], a[l]` | `int t=a[l]; a[l]=a[r]; a[r]=t;` |

### Sliding Window (Variable)
```python
def solve(arr):
    l = 0
    for r in range(len(arr)):
        # 1. Add arr[r] to state
        while condition_violated:
            # 2. Remove arr[l] from state
            l += 1
        # 3. Update max/min result
```

```java
public int solve(int[] arr) {
    int l = 0, res = 0;
    for (int r = 0; r < arr.length; r++) {
        // 1. Add arr[r]
        while (conditionViolated) {
            // 2. Remove arr[l]
            l++;
        }
        // 3. Update res
    }
    return res;
}
```
