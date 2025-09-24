import java.util.Arrays;

public class reverseusingTEMPvar {
    public static void main(String[] args) {
        int arr1[] = { 23, 3, 0, 7, 34, 0, 23, 4, 50, 0, 2 };
        int n = arr1.length;
        for (int i = 0; i < n / 2; i++) { // Only go till n/2
            int temp = arr1[i];
            arr1[i] = arr1[n-1-i];
            arr1[n-1-i] = temp;
        }
        System.out.println(Arrays.toString(arr1));
    }
}
