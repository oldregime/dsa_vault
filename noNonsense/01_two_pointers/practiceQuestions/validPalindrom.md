## 125. Valid Palindrome

### Problem Statement
Given a string `s`, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

### Solution

```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Convert to lowercase for case-insensitive comparison
        s = s.lower()
        
        # Initialize two pointers
        left = 0
        right = len(s) - 1
        
        while left < right:
            # Skip non-alphanumeric characters from left
            while left < right and not s[left].isalnum():
                left += 1
            
            # Skip non-alphanumeric characters from right
            while left < right and not s[right].isalnum():
                right -= 1
            
            # Compare characters
            if s[left] != s[right]:
                return False
            
            # Move pointers inward
            left += 1
            right -= 1
        
        return True
```

```python 
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        i = 0 
        j = len(s) - 1

        while (i<j):
            if s[i].isalnum() == False :
                i = i + 1
            elif s[j].isalnum() == False :
                j = j - 1
            elif s[i] != s[j]:
                return False
            else : 
                i = i+1
                j = j-1
        return True
```
### Key Points

1. **Case Insensitivity**: Convert the entire string to lowercase first
2. **Skip Non-Alphanumeric**: Use `isalnum()` to check if character is letter or digit
3. **Two Pointer Technique**: One pointer from start, one from end, moving towards center
4. **Early Exit**: Return False as soon as mismatch is found

### Algorithm Steps
1. Convert string to lowercase
2. Initialize left pointer at index 0, right pointer at last index
3. While left < right:
   - Skip non-alphanumeric characters from both ends
   - Compare characters at both pointers
   - If mismatch → return False
   - If match → move both pointers inward
4. Return True if all comparisons passed

### Time & Space Complexity
- **Time**: O(n) where n is the length of the string
- **Space**: O(1) - only using two pointers, no extra space