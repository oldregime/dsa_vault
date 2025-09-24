public class Max {
    static int maximum(int[] arr1){ 
        // Fixed: Missing return statement
        if (arr1 == null || arr1.length == 0) {
            return Integer.MIN_VALUE; // Return minimum value for empty array
        }
        
        int max = arr1[0];
        for (int i = 1; i < arr1.length; i++) {
            if (arr1[i] > max) {
                max = arr1[i];
            }
        }
        return max;
    }
    
    public static void main(String[] args) {
        int[] arr1 = { 23, 45, 67, 89, 12 };
        int max = maximum(arr1); // Fixed: Call the maximum method
        System.out.println("Maximum value in array: " + max);
    }

}