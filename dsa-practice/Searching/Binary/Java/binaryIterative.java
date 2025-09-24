import java.util.*; // Fixed: Removed duplicate semicolon

public class binaryIterative {
    public static void main(String[] args) {
        int[] arr1 = { 23, 54, 21, 53, 34, 1, 87, 34 };
        int target = 53;
        // int target1 = 21;
        // int target2 = 53;
        System.out.println(Arrays.toString(arr1));
        Arrays.sort(arr1);
        System.out.println(Arrays.toString(arr1));

        // Arrays.toString(arr1) for converting array to string for printing important
        // mention in notes
    

        int high = arr1.length - 1;
        int low = 0;
        int result = -1;


        while (low <= high) {
            int i= low + (high - low) / 2;
            if (arr1[i] == target) {
                result = i ;
                break;
            }
            if (arr1[i]< target) {
                low = i + 1  ;
                
            }
            if (arr1[i]> target) 
            {
                high = i -1 ;

            }
        }
        if (result != -1) {
            System.out.println("Element " + target + " found at index: " + result);
        } else {
            System.out.println("Element " + target + " not found in the array.");
        }


    }
}
