# --- BINARY SEARCH ACTIVE RECALL ---

# Type A: Classical
def binary_search(arr, target):
    left, right = 0, len(arr) - ___
    
    while ___ <= ___:
        mid = left + (___ - ___) // 2
        
        if arr[mid] == target:
            return ___
        elif arr[mid] < target:
            left = ___ + 1
        else:
            right = ___ - 1
            
    return -1

# Type B: Search Space (Binary Search on Answer)
def can_ship(capacity, packages, days):
    # Logic to check if 'capacity' works
    pass

def ship_within_days(packages, days):
    left = ___ # min possible capacity
    right = ___ # max possible capacity
    
    ans = right
    while left <= right:
        mid = left + (right - left) // 2
        if can_ship(mid, packages, days):
            ans = mid
            right = ___ - 1
        else:
            left = ___ + 1
            
    return ans
