learning while doing this :

note :
    - you can not solve 2sums using 2 pointer method :
    - as the array is not sorted rather search (`167. Two Sum II - Input Array Is Sorted`)
    - you cannot also sort the array as it will change the indices 
    - use the nested for loop method 

algorithm for 2 sum on leet code:
    1. n = len(array)
    2. create for loop for a variable i whith range(n) 
    3. create another for loop range(i+1 , n) 
    4. `retun[i,j]`

algorithm for twopointer:
    1. create 2 pointers i and j 
    2. set value one to far right and other to far left
    3. compare the sum to target 
    4. if matches return indices 
    5. if do not match 
       1. and sum is less than target then increase left pointer
       2. sum > target , then decrease* far right 
    6. `return [i,j]`


error :
    in 2sum leetcode:
        1. not using range 
        2. not using i+1 and taking nested loop range same as the original one
    in 2pointer:
        1. no decreasing and rather increasing indice on j 


points to remember:
    