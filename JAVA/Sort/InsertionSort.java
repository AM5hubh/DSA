package Sort;
public class InsertionSort {
    public static void main(String args[]){
        int nums[] = {8,7,5,6};
        System.out.println("Before Sorting");
        for(int num : nums){
            System.out.print(num+" ");
        }

        for(int i = 1;i<nums.length;i++){
            int key = nums[i];
            int j = i-1;
            while(j>=0 && nums[j]>key){
                nums[j+1]=nums[j];
                j--;
            }
            nums[j+1] = key;
        }

        System.out.println();
        System.out.println("After Sorting");
        for(int num : nums){
            System.out.print(num+" ");
        }
    }
}
