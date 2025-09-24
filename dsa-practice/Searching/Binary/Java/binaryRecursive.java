public class binaryRecursive {
    public static int search(int arr1[], int x, int low, int high) {
        if (low > high) {
            return -1; // Not found
        }
        int mid = low + (high - low) / 2;
        if (arr1[mid] == x) {
            return mid;
        } else if (arr1[mid] < x) {
            return search(arr1, x, mid + 1, high);
        } else {
            return search(arr1, x, low, mid - 1);
        }
    }

    public static void main(String[] args) {
        int[] arr1 = {1, 21, 23, 34, 34, 53, 54, 87};
        int x = 23;
        int low = 0;
        int high = arr1.length - 1;
        int result = search(arr1, x, low, high);
        if (result != -1) {
            System.out.println("Element found at index: " + result);
        } else {
            System.out.println("Element not found");
        }
    }
}
