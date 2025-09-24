class linearsearchComplex {
    public static int search(int arr[],int x){
        for (int i = 0; i < arr.length; i++) {
            if (arr[i] == x) {
                return i;                
            }
            
        }return -1;
    }
    public static void main(String[] args) {
        int[] arr = {123,123,45,7,43,21,45,23,2};
        int x = 2;
        int res = search(arr, x);
        if (res == -1) {
            System.out.println("error");
        }
        else {
            System.out.println(res);
        }

    }
    
}
