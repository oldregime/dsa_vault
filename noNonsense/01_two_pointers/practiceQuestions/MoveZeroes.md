## 283. Move Zeroes

### Question 
    - move all zero to end
    - without changin the order
    - do in place
    - Could you minimize the total number of operations done
  
```python
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        j = len(nums) - 1

        while (i<j):
            if nums[i] == 0 and nums[j] != 0 :
                nums[i],nums[j] = nums[j],nums[i]
                #“Bring a non-zero from the right to the left whenever you see a zero.”
                i += 1
                j -= 1
            elif nums[i] != 0 :
                i += 1
            else :
                j-=1
```  
### Problem Faced
    - Input: nums = [0,1,0,3,12]
    - Output: [1,3,12,0,0]
    - My Output: [12,1,3,0,0]
    - Order of non-zeros must stay: 1 → 3 → 12
    - Final: [1, 3, 12, 0, 0]
```
*Without changing the relative order of the non-zero elements*
```
So now i have decided to learn other methods to implement 2Pointer as the solution uses for loop and i only know while loop

```python
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        l = 0 
        for r in range(len(nums)):
            if nums[r] != 0 :
                nums[r],nums[l] = nums[l] ,nums[r]
                l += 1
```

## Alogrithm 
    - initialize pointer 
    - create loop with array range
    - check if value at r index if equal zero
