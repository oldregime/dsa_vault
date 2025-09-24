import java.util.*;

public class hashingbyclaude {
    
    public static void main(String[] args) {
        // HashSet Examples
        
        demonstrateHashSet();
        System.out.println("\n" + "=".repeat(50) + "\n");
        
        // HashMap Examples
        demonstrateHashMap();
        System.out.println("\n" + "=".repeat(50) + "\n");
        
        // Hash Function Examples
        demonstrateHashFunctions();
        System.out.println("\n" + "=".repeat(50) + "\n");
        
        // Collision Examples
        demonstrateCollisions();
    }
    
    // HashSet demonstration
    public static void demonstrateHashSet() {
        System.out.println("=== HashSet Examples ===");
        
        HashSet<Integer> numbers = new HashSet<>();
        
        // Adding elements
        numbers.add(10);
        numbers.add(20);
        numbers.add(30);
        numbers.add(10); // Duplicate - won't be added
        
        System.out.println("HashSet: " + numbers); // [20, 10, 30] - order not guaranteed
        System.out.println("Size: " + numbers.size()); // 3, not 4
        
        // Checking if element exists - O(1) average case
        System.out.println("Contains 20: " + numbers.contains(20)); // true
        System.out.println("Contains 40: " + numbers.contains(40)); // false
        
        // Removing elements
        numbers.remove(20);
        System.out.println("After removing 20: " + numbers);
        
        // Iterating through HashSet
        System.out.print("Elements: ");
        for(int num : numbers) {
            System.out.print(num + " ");
        }
        System.out.println();
    }
    
    // HashMap demonstration
    public static void demonstrateHashMap() {
        System.out.println("=== HashMap Examples ===");
        
        HashMap<String, Integer> studentGrades = new HashMap<>();
        
        // Adding key-value pairs
        studentGrades.put("Alice", 95);
        studentGrades.put("Bob", 87);
        studentGrades.put("Charlie", 92);
        studentGrades.put("Alice", 98); // Updates Alice's grade
        
        System.out.println("HashMap: " + studentGrades);
        
        // Accessing values - O(1) average case
        System.out.println("Alice's grade: " + studentGrades.get("Alice")); // 98
        System.out.println("David's grade: " + studentGrades.get("David")); // null
        
        // Checking if key/value exists
        System.out.println("Contains Bob: " + studentGrades.containsKey("Bob")); // true
        System.out.println("Contains grade 95: " + studentGrades.containsValue(95)); // false
        
        // Getting all keys and values
        System.out.println("All students: " + studentGrades.keySet());
        System.out.println("All grades: " + studentGrades.values());
        
        // Iterating through HashMap
        System.out.println("Student-Grade pairs:");
        for(Map.Entry<String, Integer> entry : studentGrades.entrySet()) {
            System.out.println(entry.getKey() + ": " + entry.getValue());
        }
    }
    
    // Simple hash function demonstrations
    public static void demonstrateHashFunctions() {
        System.out.println("=== Hash Function Examples ===");
        
        // Simple hash function for integers
        System.out.println("Simple Hash Functions:");
        int[] numbers = {15, 25, 35, 45};
        int tableSize = 10;
        
        for(int num : numbers) {
            int hash1 = simpleHash(num, tableSize);
            int hash2 = moduloHash(num, tableSize);
            System.out.println("Number: " + num + 
                             " | Simple Hash: " + hash1 + 
                             " | Modulo Hash: " + hash2);
        }
        
        // Hash function for strings
        System.out.println("\nString Hash Functions:");
        String[] words = {"Java", "Hash", "Table"};
        for(String word : words) {
            int hash = stringHash(word, tableSize);
            System.out.println("Word: " + word + " | Hash: " + hash);
        }
    }
    
    // Simple hash function - division method
    public static int simpleHash(int key, int tableSize) {
        return key % tableSize;
    }
    
    // Modulo hash function
    public static int moduloHash(int key, int tableSize) {
        return Math.abs(key) % tableSize;
    }
    
    // Simple string hash function
    public static int stringHash(String key, int tableSize) {
        int hash = 0;
        for(int i = 0; i < key.length(); i++) {
            hash += key.charAt(i);
        }
        return hash % tableSize;
    }
    
    // Demonstrate hash collisions
    public static void demonstrateCollisions() {
        System.out.println("=== Hash Collision Examples ===");
        
        int tableSize = 7;
        int[] keys = {10, 17, 24, 31}; // All have same hash value when mod 7
        
        System.out.println("Table Size: " + tableSize);
        System.out.println("Demonstrating collisions:");
        
        for(int key : keys) {
            int hash = key % tableSize;
            System.out.println("Key: " + key + " | Hash: " + hash);
        }
        
        System.out.println("\nAll keys have the same hash value (3) - This is a collision!");
        
        // Showing how HashSet handles this internally
        HashSet<Integer> set = new HashSet<>();
        for(int key : keys) {
            set.add(key);
        }
        System.out.println("HashSet still stores all unique values: " + set);
        System.out.println("HashSet size: " + set.size());
    }
}