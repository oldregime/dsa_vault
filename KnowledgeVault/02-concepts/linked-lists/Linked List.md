# Linked List — Fundamentals

Inspired by: GeeksforGeeks Singly Linked List tutorial (reference link below). This note is original and paraphrased—no copied text.

## What is a Linked List?

A linked list is a linear data structure where elements (nodes) are connected using pointers instead of contiguous memory. Each node stores:
- data: the value
- next: a reference to the next node (or null/None at the end)

Key idea: You get efficient insertions/deletions when you already have a reference to the position, because you only change a couple of pointers—no shifting like arrays.

Real-world analogy: Think of a treasure hunt where each clue points to the next one. You can easily insert a new clue between two clues by changing just the arrows.

## Visual intuition

![[linklist.webp]]




head -> [data|•] -> [data|•] -> [data|null]

Where • is a pointer to the next node, and head points to the first node.

## Why use a Linked List?

- Insert/delete in O(1) at known position (given a pointer/ref to node before the position)
- Grows/shrinks dynamically—no need to pre-allocate big arrays
- Great for implementing stacks, queues, adjacency lists, LRU caches, etc.

Trade-offs:
- Access by index is O(n) (sequential traversal)
- Higher memory overhead per node (store data + pointer)
- Worse cache locality than arrays

---

## Node structure

- Node = (data, next)
- Memory is non-contiguous; nodes may live anywhere in heap, connected by references
- The last node’s next is null/None

Pseudo-structure:

node:
  data: T
  next: node | null

---

## Core operations (singly list)

Contract notes:
- Inputs: head reference, optional key/value, optional position or previous node
- Outputs: possibly a new head, or boolean/found node
- Errors: invalid position, empty list, not found

1) Traversal (print/search)
- Start at head; follow next until null
- Time: O(n)

2) Insert at head
- new.next = head; head = new
- Time: O(1)

3) Insert at tail
- Traverse to last; last.next = new
- Time: O(n) without tail pointer; O(1) with maintained tail

4) Insert at position i (0-indexed)
- Traverse to i-1; link new between prev and prev.next
- Time: O(n)

5) Delete head
- head = head.next
- Time: O(1)

6) Delete by value
- Find previous node of target; prev.next = target.next
- Time: O(n)

7) Search by value
- Traverse and compare; return index or node
- Time: O(n)

Edge care: Always handle empty list and single-node list explicitly.

---

## Time and space complexity

- Access by index: O(n)
- Search: O(n)
- Insert at head: O(1)
- Insert at tail: O(1) with tail pointer, else O(n)
- Insert at position: O(n)
- Delete head: O(1)
- Delete by value/position: O(n)
- Space per node: O(1) overhead for pointer; total O(n)

Compare with arrays:
- Arrays: O(1) access, O(n) insert/delete (due to shifts)
- Linked list: O(n) access, O(1) local insert/delete

---

## Types of linked lists (quick tour)

- Singly: next pointer only (this note’s focus) — simple, memory-efficient
- Doubly: next and prev — easy delete given node, but +1 pointer overhead
- Circular: last node points back to head — useful for round-robin schedulers
- Skip list (advanced): multi-level jumps for O(log n) search/insert/delete

When to pick what:
- Mostly inserts/deletes in the middle and sequential scans: singly
- Need O(1) delete given node and bidirectional iteration: doubly
- Need round-robin behavior: circular

---

## Common edge cases

- Empty list (head = null)
- Single node (head.next = null)
- Deleting the head/tail
- Inserting at position 0 or at the end
- Invalid index (negative or beyond length)
- Potential cycles (by bug or intentionally circular)

---

## Pitfalls and tips

- Always update pointers in the right order (store next before overwriting)
- Watch off-by-one in positional operations
- In manual-memory languages, free deleted nodes; in Java/Python GC handles memory
- Maintain a tail pointer if you often append

---

## Minimal implementations

### Java (singly list)

```java
class Node {
	int data;
	Node next;
	Node(int d) { data = d; }
}

class SinglyList {
	Node head;

	// Insert at head: O(1)
	void pushFront(int x) {
		Node n = new Node(x);
		n.next = head;
		head = n;
	}

	// Insert at tail: O(n) without tail
	void pushBack(int x) {
		Node n = new Node(x);
		if (head == null) { head = n; return; }
		Node cur = head;
		while (cur.next != null) cur = cur.next;
		cur.next = n;
	}

	// Delete first occurrence of key: O(n)
	boolean deleteKey(int key) {
		if (head == null) return false;
		if (head.data == key) { head = head.next; return true; }
		Node cur = head;
		while (cur.next != null && cur.next.data != key) cur = cur.next;
		if (cur.next == null) return false;
		cur.next = cur.next.next; // unlink
		return true;
	}

	boolean search(int key) {
		Node cur = head;
		while (cur != null) {
			if (cur.data == key) return true;
			cur = cur.next;
		}
		return false;
	}
}
```

### Python (singly list)

```python
class Node:
	def __init__(self, data):
		self.data = data
		self.next = None


class SinglyList:
	def __init__(self):
		self.head = None

	def push_front(self, x):  # O(1)
		n = Node(x)
		n.next = self.head
		self.head = n

	def push_back(self, x):  # O(n)
		n = Node(x)
		if not self.head:
			self.head = n
			return
		cur = self.head
		while cur.next:
			cur = cur.next
		cur.next = n

	def delete_key(self, key):  # O(n)
		if not self.head:
			return False
		if self.head.data == key:
			self.head = self.head.next
			return True
		cur = self.head
		while cur.next and cur.next.data != key:
			cur = cur.next
		if not cur.next:
			return False
		cur.next = cur.next.next
		return True

	def search(self, key):  # O(n)
		cur = self.head
		while cur:
			if cur.data == key:
				return True
			cur = cur.next
		return False
```

---

## Interview patterns to know

- Reverse a list (iterative): prev, cur, next pointers; rewire next; O(n), O(1) extra
- Middle of list: slow/fast pointers (slow+=1, fast+=2)
- Detect cycle: Floyd’s algorithm (tortoise and hare)
- Remove Nth from end: two pointers spaced N apart
- Merge two sorted lists: iterative pointer weaving

Example: reverse iterative (Java)

```java
Node reverse(Node head) {
	Node prev = null, cur = head;
	while (cur != null) {
		Node nxt = cur.next;
		cur.next = prev;
		prev = cur;
		cur = nxt;
	}
	return prev;
}
```

Example: detect cycle (Floyd) (Python)

```python
def has_cycle(head):
	slow = fast = head
	while fast and fast.next:
		slow = slow.next
		fast = fast.next.next
		if slow is fast:
			return True
	return False
```

---

## Practice next

- Reverse a list (iterative and recursive)
- Detect a cycle and find cycle start
- Delete a node in O(1) given pointer (not head/tail edge cases)
- Merge two sorted linked lists
- Remove Nth node from end

---

## References

- GeeksforGeeks: Singly Linked List Tutorial — https://www.geeksforgeeks.org/dsa/singly-linked-list-tutorial/



