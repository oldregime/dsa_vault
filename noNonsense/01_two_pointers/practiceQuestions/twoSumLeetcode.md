```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # nums.sort()
        # i = 0
        # j = len(nums) - 1

        # while i < j:
        #     sum = nums[i] + nums[j]

        #     if sum == target:
        #         return [i, j]
        #     elif sum < target:
        #         i = i + 1
        #     else:
        #         j = j - 1
        # return [-1, -1]
        n = len(nums)

        for i in range(n):
            for j in range(i+1, n):              
                if nums[i] + nums[j] == target :
                    return [i,j]
        return []
```
