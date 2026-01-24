# Learning While Doing This

## Note:
- you can not solve 2sums using 2 pointer method :
- as the array is not sorted rather search (`167. Two Sum II - Input Array Is Sorted`)
- you cannot also sort the array as it will change the indices 
- use the nested for loop method 

## Algorithm for 2 sum on leet code:
1. n = len(array)
2. create for loop for a variable i whith range(n) 
3. create another for loop range(i+1 , n) 
4. `retun[i,j]`

## Algorithm for twopointer:
1. create 2 pointers i and j 
2. set value one to far right and other to far left
3. compare the sum to target 
4. if matches return indices 
5. if do not match 
   1. and sum is less than target then increase left pointer
   2. sum > target , then decrease* far right 
6. `return [i,j]`

## Error:
**in 2sum leetcode:**
1. not using range 
2. not using i+1 and taking nested loop range same as the original one

**in 2pointer:**
1. no decreasing and rather increasing indice on j 

---

## Event: 
i was solving moveZeroes question i was getting wrong array as i was disturbing the array of non zero elements so now i will learn other method to implemtnt for loop    

---

## ✅ The ONLY 3 Things You Actually Need to Learn

### 🔑 1️⃣ How pointers START
- Start together
- Start at both ends
- Start at different speeds

### 🔑 2️⃣ How pointers MOVE
- Move forward
- Move backward
- Move conditionally
- Move at different speeds

### 🔑 3️⃣ When pointers STOP
- When they meet
- When they cross
- When window breaks
- When condition fails

---

## Types of Two Pointer Patterns
- 🟢 1. Bi Directional
- 🟡 2. Same Direction (Fast–Slow)
- 🔵 3. Sliding Window
- 🟣 4. Fast–Slow (Different Speed)

---

## Date = 23/01/2026

---

## 1. Type A: Bi-directional Convergence

**Mechanism:** Two pointers start at opposite ends (`0` and `n-1`) and move toward each other until they meet or satisfy a condition.

**When to use:**
- The input is **sorted** (e.g., Two Sum II).
- The problem involves **symmetry** (e.g., Palindromes).
- You need to **reverse** or **swap** elements at ends.

```python
def opposite_direction(arr, target):
    left, right = 0, len(arr) - 1
    while left < right:
        curr = arr[left] + arr[right]
        if curr == target: return [left, right]
        elif curr < target: left += 1
        else: right -= 1
```

---

## 2. Type B: Equi-directional Partitioning ("Reader-Writer")

**Mechanism:**
- Both pointers start at `0`.
- `fast` (Reader): Scans every element of the array.
- `slow` (Writer): Only advances when a specific condition is met (valid element found).

**Key Concept:** This maintains the **relative order** of elements while filtering or modifying the array **in-place**.

**When to use:**
- **Removing elements** (Remove Duplicates, Remove Element).
- **Moving elements** to one side (Move Zeroes).
- Need to modify the array without making a copy (**Space Complexity O(1)**).

```python
def same_direction(arr):
    writer = 0
    for reader in range(len(arr)):
        if arr[reader] != 0: # condition to keep
            arr[writer], arr[reader] = arr[reader], arr[writer]
            writer += 1
```

---

## 3. Type C: Dynamic Sliding Window

**Mechanism:**
- **Expand Phase:** The `right` pointer increments to include new elements (grow the window).
- **Contract Phase:** If the window becomes "invalid" (violates constraints), the `left` pointer increments to exclude elements (shrink the window) until it becomes valid again.

**Key Concept:** Determining the **Longest** or **Shortest** contiguous subarray that satisfies a condition.

**When to use:**
- Problems asking for **Contiguous Subarrays** or **Substrings**.
- Keywords: "Longest substring with...", "Min size subarray sum...", "Max consecutive ones".

```python
def sliding_window(arr, k):
    left = 0
    curr = 0
    ans = 0
    for right in range(len(arr)):
        curr += arr[right]       # 1. Add
        while curr > k:          # 2. Shrink if invalid
            curr -= arr[left]
            left += 1
        ans = max(ans, right - left + 1) # 3. Update result
    return ans
```

---

## 4. Type D: Floyd's Cycle-Finding Algorithm ("Cycle Detection")

**Visual Hook:** Two runners on a track; the faster one will eventually lap the slower one if the track is a circle.

**Mechanism:** Both start at `head`.
- `slow`: Moves 1 step (`next`).
- `fast`: Moves 2 steps (`next.next`).

**When to use:**
- **Linked Lists**.
- Detecting a **Cycle**.
- Finding the **Middle Node** in a single pass (when Fast hits end, Slow is at middle).

```python
def has_cycle(head):
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast: return True
    return False
```