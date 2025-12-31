public class skeleton {

    public static void main(String Args) {

        int[] arr = {1, 2, 3, 4, 5, 9};
        int target = 12 ;
        int i = 0 ,j = arr.length - 1 ;
        while(i<j){
            int sum = arr[i] + arr[j];
            if (sum == target){
                System.out.println(i + " " + j );
                break;
            }
            else if (sum < target) {
                i++
            }
            else
        }


    }
    
}
