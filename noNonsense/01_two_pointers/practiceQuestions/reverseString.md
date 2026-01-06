## 344. Reverse String

```python 
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i = 0 
        j = len(s) - 1 

        while (i<j):
            s[i],s[j] = s[j],s[i]
            # temp = s[i]
            # s[i] = s[j]  
            # s[j] = temp
           
            i = i + 1 
            j = j - 1
```
question : 
    - must modify sthe given string in place 
    - should not create another list

algorithm : 
    1. exchange value at pointer i and j 
    2. increment and decrement pointer accordingly
