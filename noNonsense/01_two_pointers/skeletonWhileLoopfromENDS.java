import java.util.ArrayList;
import java.util.List;

public class skeletonWhileLoopfromENDS {

    public static void main(String[] args) {

        int[] arr = {1, 2, 3, 4, 5,6,7,8,9,10};
        int target = 12 ;
        int i = 0 ,j = arr.length - 1 ;
        List<int[]> result = new ArrayList<>();

        while(i<j){
            int sum = arr[i] + arr[j];
            if (sum == target){
                result.add(new int[]{i,j});
                System.out.println(i + " " + j );
                break;
            }

            else if (sum < target) {
                i++;
            }
            else{
                j--;
            }
        }
        for (int[] pair : result){
            System.out.println(pair[0] + " " + pair[1]);
        }


    }
    
}
