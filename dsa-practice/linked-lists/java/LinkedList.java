public class LinkedList {
    // Node class for LinkedList
    static class Node {
        int data;
        Node next;
        
        Node(int data) {
            this.data = data;
            this.next = null;
        }
    }
    
    // Head of the LinkedList
    private Node head;
    
    // Constructor
    public LinkedList() {
        this.head = null;
    }
    
    // Add a node at the beginning
    public void push(int data) {
        Node newNode = new Node(data);
        newNode.next = head;
        head = newNode;
    }
    
    // Add a node at the end
    public void append(int data) {
        Node newNode = new Node(data);
        
        // If list is empty
        if (head == null) {
            head = newNode;
            return;
        }
        
        // Find the last node
        Node last = head;
        while (last.next != null) {
            last = last.next;
        }
        
        // Append the new node
        last.next = newNode;
    }
    
    // Print the LinkedList
    public void printList() {
        Node current = head;
        System.out.print("LinkedList: ");
        while (current != null) {
            System.out.print(current.data + " → ");
            current = current.next;
        }
        System.out.println("null");
    }
    
    // Main method for testing
    public static void main(String[] args) {
        LinkedList list = new LinkedList();
        
        // Test operations
        list.append(10);
        list.push(5);
        list.append(20);
        list.push(1);
        
        // Print the list
        list.printList();
    }
}