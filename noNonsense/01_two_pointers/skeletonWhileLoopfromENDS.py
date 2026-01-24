# Initialize one pointer at the start of the array and another at the end.
# Calculate the sum of elements at these two pointers.
# If the sum equals the target, return the indices (or record if multiple solutions exist).
# If the sum is less than the target, move the left pointer forward to increase the sum.
# If the sum is greater than the target, move the right pointer backward to decrease the sum.
# Repeat this process until the pointers meet or a solution is found.
# If multiple pairs satisfy the sum, track and return the pair with the minimum indices.


# 1. Problem in Plain English
# We have a sorted list of numbers.
# We need two different positions whose numbers add to a target.
# Return the positions, not the values.
# Example:
# [1, 3, 4, 7], target = 5 → positions 0 and 2 (because 1 + 4 = 5).

target = 12
i = 0 
arr = [1,2,3,4,5,8,9 ,11]

j = len(arr) - 1 
ans = []


while i < j :
    sum = arr[i] + arr[j]
    if sum == target :
        ans.append([i,j])
        i+=1
        j-=1
    elif sum < target :
        i = i + 1 # increase the right to left pointer
    else :
        j = j - 1 #make sure to decrease the right to left pointer
    
        
print(ans)