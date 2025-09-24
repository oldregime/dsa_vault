# Two Sum - LeetCode 001

## 📋 Problem Statement
Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

## 🎯 Examples
### Example 1:
**Input:** nums = [2,7,11,15], target = 9
**Output:** [0,1]
**Explanation:** Because nums[0] + nums[1] == 9, we return [0, 1].

### Example 2:
**Input:** nums = [3,2,4], target = 6
**Output:** [1,2]
**Explanation:** Because nums[1] + nums[2] == 6, we return [1, 2].

## 💭 Approach

### Method 1: Brute Force
1. Use nested loops to check every pair
2. If sum equals target, return indices
3. Time: O(n²), Space: O(1)

### Method 2: HashMap (Optimal)
1. Create HashMap to store (value → index)
2. For each element, calculate complement = target - current
3. If complement exists in map, return [complement_index, current_index]
4. Otherwise, add current element to map
5. Time: O(n), Space: O(n)

**Time Complexity:** O(n)
**Space Complexity:** O(n)

## 💡 Solution

### Java
```java
public int[] twoSum(int[] nums, int target) {
    Map<Integer, Integer> map = new HashMap<>();
    
    for (int i = 0; i < nums.length; i++) {
        int complement = target - nums[i];
        
        if (map.containsKey(complement)) {
            return new int[]{map.get(complement), i};
        }
        
        map.put(nums[i], i);
    }
    
    throw new IllegalArgumentException("No solution found");
}
```

### Python
```python
def twoSum(nums, target):
    seen = {}
    
    for i, num in enumerate(nums):
        complement = target - num
        
        if complement in seen:
            return [seen[complement], i]
        
        seen[num] = i
    
    return []
```

## 🧠 Key Insights
- HashMap provides O(1) average lookup time
- We only need one pass through the array
- Store value as key and index as value in HashMap
- Check for complement before adding current element to avoid using same element twice

## 🔗 Related Problems
- [[Three Sum]]
- [[Four Sum]]
- [[Two Sum II - Input Array is Sorted]]

## 📈 Difficulty Progression
- **Next:** [[Valid Parentheses]] - Stack basics
- **Harder:** [[Three Sum]] - Similar pattern with three numbers

---
Tags: #problem/leetcode #difficulty/easy #concept/arrays #concept/hashing #pattern/two-pointer
Status: #status/solved
Date Solved: 2025-09-23
