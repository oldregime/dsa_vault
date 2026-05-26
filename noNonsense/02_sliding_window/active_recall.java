// --- SLIDING WINDOW ACTIVE RECALL ---

public class SlidingWindow {
    // Type A: Fixed Size
    public int fixedWindow(int[] arr, int k) {
        int currSum = 0;
        for (int i = 0; i < ___; i++) currSum += arr[i];
        int maxSum = currSum;

        for (int i = 0; i < arr.length - ___; i++) {
            currSum = currSum - arr[___] + arr[i + ___];
            maxSum = Math.max(maxSum, ___);
        }
        return maxSum;
    }

    // Type B: Variable Size
    public int variableWindow(int[] arr, int target) {
        int left = 0, currSum = 0, res = Integer.MAX_VALUE;
        for (int right = 0; right < arr.length; right++) {
            currSum += arr[___];
            while (___ >= target) {
                res = Math.min(res, ___ - ___ + 1);
                currSum -= arr[___];
                ___++;
            }
        }
        return res == Integer.MAX_VALUE ? 0 : res;
    }
}
