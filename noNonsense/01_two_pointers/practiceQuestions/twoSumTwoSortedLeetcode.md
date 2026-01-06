```python
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers) - 1


        while (i < j ):
            sum = numbers[i] + numbers[j]

            if sum == target :
                return [i+1,j+1]
            elif sum < target : 
                i = i + 1 
            else : 
                j = j - 1
        return [-1,-1]
```

question : 
    - it was a 1-indexed array therefore had to use `return [i+1,j+1]`
    - exactly one solution
    - sorted in non-decreasing order ~ asscending order 
  
points : 
    - return [i+1,j+1] because 1 indexed array
    - 4️⃣ Important Rule (Memorize This)

Internal logic → always 0-based indexing  this is when asked indices
Output → convert to required indexing this is when asked positions