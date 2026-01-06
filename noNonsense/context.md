# 📋 DSA Learning Master Plan

> **Philosophy**: Move from being a "collector" to "retriever" — Focus on DOING, not hoarding.

---

## 📊 Current Progress Analysis

### ✅ What You've Done Well
1. **Structured note-taking** - You document errors, algorithms, and points to remember
2. **Learning from mistakes** - You actively track what went wrong (e.g., MoveZeroes order issue)
3. **Understanding pattern variations** - You identified the 4 sub-types of two pointers
4. **Practical application** - You're solving real LeetCode problems, not just watching videos

### ⚠️ What Needs Improvement

| Issue | Evidence | Fix |
|-------|----------|-----|
| **Only know ONE implementation style** | MoveZeroes failed because you only knew while-loop with both-ends approach | Learn all 4 pointer movement patterns with code |
| **Notes are scattered** | Algorithm steps mixed with errors, no clear separation | Use consistent template (see below) |
| **Skeleton files incomplete** | Only covers opposite-direction pattern | Create skeleton for EACH sub-pattern |
| **Missing difficulty progression** | Jumped between easy problems randomly | Follow the ordered problem list below |
| **No active recall practice** | Notes exist but no blank-fill templates | Create `template.py` with blanks to fill daily |
| **Incomplete problem solutions** | MoveZeroes has incomplete algorithm section | Always complete all sections before moving on |

---

## 🎯 The 3 Core Rules (Memorize)

### 🔑 Rule 1: How Pointers START
```
┌─────────────────────────────────────────────┐
│ OPPOSITE ENDS    →  left = 0, right = n-1   │
│ SAME POSITION    →  slow = 0, fast = 0      │
│ DIFFERENT SPEED  →  slow = head, fast = head│
└─────────────────────────────────────────────┘
```

### 🔑 Rule 2: How Pointers MOVE
```
┌─────────────────────────────────────────────┐
│ SHRINK WINDOW    →  left++, right--         │
│ EXPAND WINDOW    →  right++ (fast moves)    │
│ CONDITIONAL      →  move based on condition │
│ SPEED DIFFERENCE →  slow+1, fast+2          │
└─────────────────────────────────────────────┘
```

### 🔑 Rule 3: When Pointers STOP
```
┌─────────────────────────────────────────────┐
│ MEET/CROSS       →  while (left < right)    │
│ END OF ARRAY     →  while (fast < n)        │
│ CYCLE DETECTED   →  when slow == fast       │
│ CONDITION FAILS  →  when window invalid     │
└─────────────────────────────────────────────┘
```

---

## 📚 Pattern 1: Two Pointers (4 Sub-Patterns)

### 🟢 Type A: Opposite Direction (Both Ends)
**When to use**: Sorted array, palindrome check, container problems
**Template**:
```python
def opposite_direction(arr):
    left, right = 0, len(arr) - 1
    
    while left < right:
        # Process arr[left] and arr[right]
        if condition_met:
            return result
        elif need_larger:
            left += 1
        else:
            right -= 1
```
**Problems**: Two Sum II ✅, Valid Palindrome ✅, Reverse String ✅, Container With Most Water ⬜

---

### 🟡 Type B: Same Direction (Reader-Writer / Slow-Fast Index)
**When to use**: In-place modifications, remove elements, partition
**Template**:
```python
def same_direction(arr):
    writer = 0  # slow pointer - where to write
    
    for reader in range(len(arr)):  # fast pointer - reads all
        if should_keep(arr[reader]):
            arr[writer] = arr[reader]
            # OR swap: arr[writer], arr[reader] = arr[reader], arr[writer]
            writer += 1
    
    return writer  # new length or modified array
```
**Problems**: Move Zeroes ✅, Remove Duplicates ⬜, Remove Element ⬜

---

### 🔵 Type C: Sliding Window (Variable Size)
**When to use**: Subarray/substring with condition, max/min window
**Template**:
```python
def sliding_window(arr, k):
    left = 0
    window_state = {}  # or sum, count, etc.
    result = 0
    
    for right in range(len(arr)):
        # Add arr[right] to window
        
        while window_invalid:
            # Remove arr[left] from window
            left += 1
        
        # Update result
        result = max(result, right - left + 1)
    
    return result
```
**Problems**: Longest Substring Without Repeating ⬜, Max Consecutive Ones III ⬜

---

### 🟣 Type D: Fast-Slow (Different Speed)
**When to use**: Linked list cycle, find middle, happy number
**Template**:
```python
def fast_slow(head):
    slow, fast = head, head
    
    while fast and fast.next:
        slow = slow.next        # 1 step
        fast = fast.next.next   # 2 steps
        
        if slow == fast:
            return True  # cycle detected
    
    return False
```
**Problems**: Linked List Cycle ⬜, Middle of Linked List ⬜, Happy Number ⬜

---

## 📝 Problem Tracking: Two Pointers

### Ordered Problem List (Do in this exact order)

| # | Problem | Type | Difficulty | Status | Date | Attempts |
|---|---------|------|------------|--------|------|----------|
| 1 | 344. Reverse String | A | Easy | ✅ | - | - |
| 2 | 125. Valid Palindrome | A | Easy | ✅ | - | - |
| 3 | 167. Two Sum II | A | Medium | ✅ | - | - |
| 4 | 283. Move Zeroes | B | Easy | ✅ | - | - |
| 5 | 26. Remove Duplicates from Sorted Array | B | Easy | ⬜ | - | - |
| 6 | 27. Remove Element | B | Easy | ⬜ | - | - |
| 7 | 977. Squares of Sorted Array | A | Easy | ⬜ | - | - |
| 8 | 11. Container With Most Water | A | Medium | ⬜ | - | - |
| 9 | 15. 3Sum | A | Medium | ⬜ | - | - |
| 10 | 75. Sort Colors | B | Medium | ⬜ | - | - |
| 11 | 141. Linked List Cycle | D | Easy | ⬜ | - | - |
| 12 | 876. Middle of Linked List | D | Easy | ⬜ | - | - |
| 13 | 202. Happy Number | D | Easy | ⬜ | - | - |
| 14 | 142. Linked List Cycle II | D | Medium | ⬜ | - | - |
| 15 | 42. Trapping Rain Water | A | Hard | ⬜ | - | - |

---

## 📋 Standard Note Template (Use for EVERY problem)

```markdown
## [Number]. [Problem Name]

### 📖 Question Summary
- Point 1
- Point 2
- Constraints

### 🧠 Pattern Identified
Type: [A/B/C/D] - [Name]
Why: [1 sentence reason]

### 💻 Solution
\```python
# code here
\```

### ⚙️ Algorithm Steps
1. Step 1
2. Step 2
3. Step 3

### ❌ Errors Made
1. Error description → Fix

### 💡 Key Insight
One sentence that captures the core trick

### 🔁 Review Status
- [ ] Solved independently
- [ ] Solved with hint
- [ ] Need to redo
```

---

## 📅 Daily Practice Routine

### Morning (15 min)
1. Open `skeleton.py` → close it → rewrite from memory
2. Pick ONE problem from the list above
3. Try to solve WITHOUT looking at notes (set 20 min timer)

### If Stuck
1. Check ONLY the pattern type (A/B/C/D)
2. Write the template skeleton first
3. Then fill in problem-specific logic

### After Solving
1. Fill in the note template completely
2. Mark the problem in tracking table
3. If failed: schedule redo for next day

---

## 🚫 Anti-Patterns to Avoid

| ❌ DON'T | ✅ DO |
|----------|-------|
| Watch 5 videos on same topic | Solve 1 problem, then 1 video max |
| Copy-paste solutions | Type every character yourself |
| Skip problems that feel hard | Struggle for 20 min, then check |
| Leave notes incomplete | Complete all sections before moving on |
| Move to next pattern before mastering | 10+ problems before new pattern |

---

## 🎯 Weekly Goals

### Week 1: Two Pointers Type A + B
- [ ] Complete problems 1-7
- [ ] Create blank-fill template
- [ ] Rewrite skeleton from memory 5 times

### Week 2: Two Pointers Type C + D
- [ ] Complete problems 8-15
- [ ] All notes complete with template
- [ ] Can solve any Type A/B without notes

### Week 3: Sliding Window Pattern
- [ ] Move to next pattern folder
- [ ] Apply same structure

---

## 📌 Important Rules (Memorize)

```
┌─────────────────────────────────────────────────────────────┐
│ 1. Internal logic → always 0-based indexing                 │
│ 2. Output → convert to required indexing (1-based if asked) │
│ 3. Can't use two-pointer on unsorted for index problems     │
│ 4. Same-direction = FOR loop, Opposite = WHILE loop         │
│ 5. When order matters → use same-direction (reader-writer)  │
└─────────────────────────────────────────────────────────────┘
```

---

## 🔧 Python Must-Know

```python
# Data Structures
list, dict, set, deque, heapq

# Control Flow
for, while, if-elif-else, def

# Operations
slicing: arr[start:end:step]
sorting: arr.sort(), sorted(arr, key=lambda x: x[1])
string: s.lower(), s.isalnum(), s.split()

# Two Pointer Specific
len(arr) - 1          # last index
arr[left], arr[right] = arr[right], arr[left]  # swap
range(len(arr))       # for same-direction
while left < right:   # for opposite-direction
```

---

## 📈 Pattern Mastery Roadmap

```
Current: ████░░░░░░░░░░░ Two Pointers (4/15 problems)

1. Two Pointers       ████░░░░░░░░░░░ [IN PROGRESS]
2. Sliding Window     ░░░░░░░░░░░░░░░ [NEXT]
3. Fast & Slow        ░░░░░░░░░░░░░░░
4. Binary Search      ░░░░░░░░░░░░░░░
5. Merge Intervals    ░░░░░░░░░░░░░░░
... (continue from guideline.md)
```

---

*Last Updated: 2026-01-04*