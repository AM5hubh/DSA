package Sort;

public class MergeSort {
    public static void mergerSort(int[] arr, int l, int r) {
        if (l < r) {
            int mid = (l + r) / 2;
            mergerSort(arr, l, mid);
            mergerSort(arr, mid + 1, r);
            merge(arr, l, mid, r);
        }
    }

    private static void merge(int[] arr, int l, int mid, int r) {
        
        int n1 = mid-l+1;
        int n2 = r-mid;
        
        int lArr[] = new int[n1];
        int rArr[] = new int[n2];

        for(int x = 0;x<n1;x++){
            lArr[x] = arr[l+x];
        }
        for(int x = 0;x<n2;x++){
            rArr[x] = arr[mid+1+x];
        }
        // System.out.println( "left ");
        // for (int element : lArr) {

        //     System.out.print(element + " ");
        // }
        // System.out.println("right ");
        // for (int element : rArr) {
        //     System.out.print(element + " ");
        // }

        int i = 0;
        int j = 0;
        int k = l;
        while(i<n1 && j<n2){
            if(lArr[i] <= rArr[j]){
                arr[k] = lArr[i];
                i++;
            }
            else{
                arr[k] = rArr[j];
                j++;
            }
            k++;
        }
        while(i<n1){
            arr[k] = lArr[i];
            i++;
            k++;
        }
        while(j<n2){
            arr[k] = rArr[j];
            j++;
            k++;
        }

    }

    public static void main(String[] args) {
        int arr[] = { 8,5,9,1,6,7 };
        System.out.println("Before Sorting");
        for (int element : arr) {
            System.out.print(element + " ");
        }
        System.out.println();

        mergerSort(arr, 0, arr.length - 1);

        System.out.println("After Sorting");
        for (int element : arr) {
            System.out.print(element + " ");
        }
    }
}
