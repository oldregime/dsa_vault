// --- TWO POINTERS ACTIVE RECALL ---

public class TwoPointers {
    // Type A: Opposite Ends
    public int[] oppositeEnds(int[] arr, int target) {
        int left = ___, right = ___;
        while (___ < ___) {
            int curr = arr[___] + arr[___];
            if (curr == target) return new int[]{___, ___};
            else if (curr < target) ___++;
            else ___--;
        }
        return new int[]{};
    }

    // Type B: Reader-Writer
    public int readerWriter(int[] arr) {
        int writer = ___;
        for (int reader = 0; reader < arr.length; reader++) {
            if (shouldKeep(arr[reader])) {
                int temp = arr[writer];
                arr[writer] = arr[reader];
                arr[reader] = temp;
                ___++;
            }
        }
        return writer;
    }
}
