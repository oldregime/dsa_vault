
public class basic {

    static void bubblesort(int arr[], int n) {
        int k , k2 , temp ;
        boolean swapcheck = false;
        

        
        for ( k = 0; k < n - 1; k++) {
            swapcheck = false ;
            for ( k2 = 0; k2 < n - k - 1; k2++) {
                //swap
                if (arr[k2]> arr[k]) {
                    temp = arr[k2];
                    arr[k2] = arr[k];
                    arr[k] = temp;
                    swapcheck = true;
                }
                
            }
            
            
        }
        if (swapcheck == false) {
                System.out.println("No swapping");
                
            }

        
    }

    static void printarr(int arr[], int n) {
        for (int i = 0; i < arr.length; i++) {
            System.out.print(arr[i]+" ");
            
        }System.out.println("");

    }

    public static void main(String args[]) {
        int arr[] = {5, 1, 4, 2, 8};
        int n = arr.length;
        bubblesort(arr, n);
        System.out.print("Sorted Arr = ");
        printarr(arr, n);

    }
}