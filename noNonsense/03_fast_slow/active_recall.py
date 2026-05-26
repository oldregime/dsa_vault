# --- FAST & SLOW ACTIVE RECALL ---

# Type A: Cycle Detection
def has_cycle(head):
    slow, fast = ___, ___
    
    while ___ and ___.next:
        slow = slow.___
        fast = fast.___.next
        
        if slow == ___:
            return True
            
    return False

# Type B: Find Middle
def find_middle(head):
    slow, fast = head, head
    
    while ___ and ___.next:
        slow = slow.___
        fast = fast.___.next
        
    return ___ # Slow is at the middle
