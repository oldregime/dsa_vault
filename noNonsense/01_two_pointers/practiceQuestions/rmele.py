def removeElement(nums, val):
    w = 0 
    n = len(nums)
    for r in range(n):
        if nums[r] != val:
            nums[r], nums[w] = nums[w], nums[r]
            w += 1
    return w

# Test with sample input
nums = [3, 2, 2, 3]
print(nums)
val = 3
k = removeElement(nums, val)
print("Valid length:", k)
print("Array:", nums[:k])
print(nums)