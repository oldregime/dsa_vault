# --- SLIDING WINDOW ACTIVE RECALL ---

# Type A: Fixed Size
def fixed_window(arr, k):
    # 1. Initialize first window
    curr_sum = sum(arr[:___])
    max_sum = curr_sum
    
    # 2. Slide
    for i in range(len(arr) - ___):
        curr_sum = curr_sum - arr[___] + arr[i + ___]
        max_sum = max(max_sum, ___)
    
    return max_sum

# Type B: Variable Size (Shrinkable)
def variable_window(arr, target):
    left = 0
    curr_sum = 0
    res = float('inf')
    
    for right in range(len(arr)):
        # 1. Expand
        curr_sum += arr[___]
        
        # 2. Shrink while valid
        while ___ >= target:
            res = min(res, ___ - ___ + 1)
            curr_sum -= arr[___]
            ___ += 1
            
    return res if res != float('inf') else 0
