import java.util.*;
/*
 * Move All Zeroes to End
Difficulty: EasyAccuracy: 45.51%Submissions: 342K+Points: 2Average Time: 15m

You are given an array arr[] of non-negative integers. Your task is to move all the zeros in the array to the right end while maintaining the relative order of the non-zero elements. The operation must be performed in place, meaning you should not use extra space for another array.

Examples:

Input: arr[] = [1, 2, 0, 4, 3, 0, 5, 0]
Output: [1, 2, 4, 3, 5, 0, 0, 0]
Explanation: There are three 0s that are moved to the end.

Input: arr[] = [10, 20, 30]
Output: [10, 20, 30]
Explanation: No change in array as there are no 0s.

Input: arr[] = [0, 0]
Output: [0, 0]
Explanation: No change in array as there are all 0s.

Constraints:
1 ≤ arr.size() ≤ 105
0 ≤ arr[i] ≤ 105
 */

public class zerotoback {
    public static void main(String[] args) {
        ArrayList<Integer> arr= new ArrayList<>();
        int arr12[] = {23,3,0,7,34,0,23,4,50,0,2};
        int count = 0;
        for (int i = 0; i < arr12.length; i++) {
            if (arr12[i] != 0 ) {
                int n = arr12[i];
                arr.add(n);  
                   
            }
            if (arr12[i]==0) {
                count++;
                
            }       
            
        }
        for (int j = 0; j < count; j++) {
            arr.add(0);
            
        }System.out.println(arr);
        
        
        
    }
}
