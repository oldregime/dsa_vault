import java.util.*;

public class basic {
    public static void main(String[] args){
        //creating a hashmap
        HashMap<String, Integer> map = new HashMap<>(); // Fixed: Hashmap -> HashMap

        //key value pairs
        map.put("Alice", 85);
        map.put("Bob", 90); 
        map.put("Charlie", 78);

        //retrieval
        System.out.println("Bob's score: " + map.get("Bob")); // Fixed: "bob" -> "Bob" (case-sensitive)
        
        // Additional operations
        System.out.println("All entries: " + map);
        
        // Check if key exists
        System.out.println("Contains Alice? " + map.containsKey("Alice"));
        
        // Update value
        map.put("Charlie", 85);
        System.out.println("Updated map: " + map);
    }



}