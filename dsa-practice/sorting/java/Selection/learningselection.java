public class learningselection {

    static class Sorting {

        static void selectionSort(int[] arr) {
            int n = arr.length;

            for (int i = 0; i < n; i++) {
                int minIndex = i;

                for (int j = i + 1; j < n; j++) {
                    if (arr[j] < arr[minIndex]) {
                        minIndex = j;
                    }
                }

                int temp = arr[minIndex];
                arr[minIndex] = arr[i];
                arr[i] = temp;
            }

        }

        static void printsorted(int arr[]) {
            for (int i = 0; i < arr.length; i++) {
                System.out.print(arr[i] + " ");
            }
        }
    }

    public static void main(String[] args) {
        int arr[] = { 64, 22, 25, 28, 95, 82 };
        System.out.println("original : ");
        Sorting.printsorted(arr);

        Sorting.selectionSort(arr);

        System.out.println("");
        System.out.println("sorted : ");
        Sorting.printsorted(arr);

    }

}
