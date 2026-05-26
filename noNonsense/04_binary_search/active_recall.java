// --- BINARY SEARCH ACTIVE RECALL ---

public class BinarySearch {
    // Type A: Classical
    public int binarySearch(int[] arr, int target) {
        int left = 0, right = arr.length - ___;
        while (___ <= ___) {
            int mid = left + (___ - ___) / 2;
            if (arr[mid] == target) return ___;
            else if (arr[mid] < target) left = ___ + 1;
            else right = ___ - 1;
        }
        return -1;
    }

    // Type B: Search Space
    public int shipWithinDays(int[] packages, int days) {
        int left = ___, right = ___; // min and max possible
        int ans = right;
        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (canShip(mid, packages, days)) {
                ans = mid;
                right = ___ - 1;
            } else {
                left = ___ + 1;
            }
        }
        return ans;
    }
}
