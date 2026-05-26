# --- TWO POINTERS ACTIVE RECALL ---

# Type A: Opposite Ends
# Use: Sorted arrays, Palindromes
def opposite_ends(arr, target):
    left, right = ___, ___
    while ___ < ___:
        curr = arr[___] + arr[___]
        if curr == target:
            return [___, ___]
        elif curr < target:
            ___ += 1
        else:
            ___ -= 1
    return []

# Type B: Reader-Writer (Same Direction)
# Use: In-place removal, Moving elements
def reader_writer(arr):
    writer = ___
    for reader in range(len(arr)):
        if condition(arr[reader]):
            arr[writer], arr[reader] = arr[reader], arr[writer]
            ___ += 1
    return writer
