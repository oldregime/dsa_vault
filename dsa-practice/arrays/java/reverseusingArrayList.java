import java.util.*;

public class reverseusingArrayList {
    public static void main(String[] args) {
        ArrayList<Integer> arr = new ArrayList<>();
    int arr1[] = {23,3,0,7,34,0,23,4,50,0,2};
    int n = arr1.length;

   System.out.println(n);
    /*
     * for (int i = n - 1; i >= 0; i--) {
            arr.add(arr1[i]);
        }
     */
    
    for (int i = n-1; i >=0; i--) {
        arr.add(arr1[i]);
        
    }
    System.out.println(arr);
    }
    
}
