import java.util.ArrayList;
import java.util.Collections;

public class Leadersinarray {
    
    static ArrayList<Integer> leaders(int arr[]) {
        ArrayList<Integer> result = new ArrayList<>();
        int n = arr.length;
        
        // The rightmost element is always a leader
        int maxFromRight = arr[n-1];
        result.add(maxFromRight);
        System.out.println(result); // Fixed: Arrays.toString() doesn't work on ArrayList
        // Start from the second rightmost element
        for (int i = n-2; i >= 0; i--) {
            // If current element is greater than or equal to max so far
            if (arr[i] >= maxFromRight) {
                maxFromRight = arr[i];
                result.add(maxFromRight);
            }
        }
        
        // Since we added elements from right to left, reverse the result
        Collections.reverse(result);
        
        return result;
    }
    
    // Main method for testing
    public static void main(String[] args) {
        // Test case 1
        int[] arr1 = {16, 17, 4, 3, 5, 2};
        ArrayList<Integer> result1 = leaders(arr1);
        System.out.println("Test Case 1: " + result1);  // Expected: [17, 5, 2]
        
        // Test case 2
        int[] arr2 = {10, 4, 2, 4, 1};
        ArrayList<Integer> result2 = leaders(arr2);
        System.out.println("Test Case 2: " + result2);  // Expected: [10, 4, 4, 1]
        
        // Test case 3
        int[] arr3 = {5, 10, 20, 40};
        ArrayList<Integer> result3 = leaders(arr3);
        System.out.println("Test Case 3: " + result3);  // Expected: [40]
        
        // Test case 4
        int[] arr4 = {30, 10, 10, 5};
        ArrayList<Integer> result4 = leaders(arr4);
        System.out.println("Test Case 4: " + result4);  // Expected: [30, 10, 10, 5]
    }
}


