
public class Array {
    public static void main(String[] args) {
    //     System.out.println("Hello, World!");
    //    int[] arr1  = {1, 2, 3, 4, 5};
    //    int n = arr1.length;
    //    int arr[] = { 23, 45, 67, 89, 12};

    //    for (int i = 0 ; n > i ; i++){
    //           System.out.println(arr1[i]);
    //           System.out.println(arr[i]);
    //    }

    int[] array1 = new int[5];
    char[] array2 = new char[5];
    float[] array3 = new float[5];
    int[] array4 = new int[5]; // Fixed: Incorrect array declaration syntax
    array2 = new char[]{ 'a', 'b', 'c', 'd', 'e' };
    int arr1[] = { 1, 2, 3, 4, 5 };
    char arr2[] = { 'a', 'b', 'c', 'd', 'e' };
    float arr3[] = { 1.4f, 2.0f, 24f, 5.0f, 0.0f };
    String[] arr = { "Hello", "World", "Java", "Programming", "Language" };
    System.out.println("Integer Array:");
    for (int i = 0; i < array1.length; i++) {
        System.out.print(array1[i] + " ");
    }
    System.out.println("\narr1 contents:");
    for (int i = 0; i < arr1.length; i++) {
        System.out.print(arr1[i] + " ");
    }
    System.out.println("\nChar Array:");
    for (int i = 0; i < array2.length; i++) {
        System.out.print(array2[i] + " ");
    }
    System.out.println("\narr2 contents:");
    for (int i = 0; i < arr2.length; i++) {
        System.out.print(arr2[i] + " ");
    }
    System.out.println("\nFloat Array:");
    for (int i = 0; i < array3.length; i++) {
        System.out.print(array3[i] + " ");
    }
    System.out.println("\narr3 contents:");
    for (int i = 0; i < arr3.length; i++) {
        System.out.print(arr3[i] + " ");
    }
    System.out.println("\nString Array:");
    for (int i = 0; i < arr.length; i++) {
        System.out.print(arr[i] + " ");
    }
    System.out.println();


    }
}
