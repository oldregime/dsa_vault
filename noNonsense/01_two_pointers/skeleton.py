arr = [1,2,3,4,5,6,7,8,9,10]
target = 12 

l = 0 
r = len(arr) - 1

while l < r :
    sum = arr[l] + arr[r]

    if sum == target :
        print([l,r])
        l += 1 
        r -= 1 
    elif sum < target :
        l += 1
    else :
        r -= 1 

