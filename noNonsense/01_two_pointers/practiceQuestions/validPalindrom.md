## 125 Valid Palindrom 

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

### question : 
    - given a string with various types of charachters and Cases
    - Ignore all NON-alphanumeric characters
    - homogenise the Cases 
    - compare and check if the string is palindrome and return BOOL

### errors : 
    1. need to seprately check if both are alphnumeric
    2. `make sure to write case for both condition`
       1. condition 1 - not equal return false
       2. condition 2 - both are equal so so check other char and move on 

### points to remember : 

### algorithm:
    1. convert all letters to lower case using keyword s = s.lower()
    2. initialize pointers
    3. run a while loop with check that pointer dont cross
    4. check if value at pointer i is alphnumeric
       1. if yes = then okay
       2. if no = skip and move on to next
    5. do same for j
    6. check if value at i and j is same 
    7. else(meaning both are same and we can move on to next chars's) : 
       1. increment i and decrease j and run the loop
   

### notes:
