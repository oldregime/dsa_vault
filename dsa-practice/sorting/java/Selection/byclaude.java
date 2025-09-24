public class byclaude {
    static class Sorting{
        static void selectionSort(int[] arr){
            int n = arr.length;
            
            // One by one move boundary of unsorted part
            for (int i = 0; i < n-1; i++) {
                // Find the minimum element in unsorted array
                int minIndex = i;
                for (int j = i+1; j < n; j++) {
                    if (arr[j] < arr[minIndex]) {
                        minIndex = j;
                    }
                }
                
                // Swap the found minimum element with the first element
                int temp = arr[minIndex];
                arr[minIndex] = arr[i];
                arr[i] = temp;
            }
        }
        
        static void printArray(int arr[]) {
            for (int i=0; i < arr.length; i++) {
                System.out.print(arr[i] + " ");
            }
            System.out.println();
        }
    }
    
    public static void main(String[] args) {
        int arr[] = {64, 34, 25, 12, 22, 11, 90};
        
        System.out.println("Original array:");
        Sorting.printArray(arr);
        
        Sorting.selectionSort(arr);
        
        System.out.println("Sorted array:");
        Sorting.printArray(arr);
    }
}