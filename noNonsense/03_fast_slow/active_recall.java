// --- FAST & SLOW ACTIVE RECALL ---

class ListNode { int val; ListNode next; }

public class FastSlow {
    // Type A: Cycle Detection
    public boolean hasCycle(ListNode head) {
        ListNode slow = ___, fast = ___;
        while (___ != null && ___.next != null) {
            slow = slow.___;
            fast = fast.___.next;
            if (slow == ___) return true;
        }
        return false;
    }

    // Type B: Find Middle
    public ListNode findMiddle(ListNode head) {
        ListNode slow = head, fast = head;
        while (___ != null && ___.next != null) {
            slow = slow.___;
            fast = fast.___.next;
        }
        return ___;
    }
}
