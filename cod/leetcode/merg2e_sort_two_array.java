package corejava;

import java.util.Arrays;

public class merg2e_sort_two_array {
	public static void main(String[] args) {
        int[] arr1 = { 9, 3, 5, 1, 7 };
        int[] arr2 = { 8, 4, 6, 2 };
        int[] result = new int[arr1.length + arr2.length];

        // Gộp hai mảng và sắp xếp chúng
        merge(arr1, arr2, result);

        // Hiển thị kết quả
        System.out.println("Merged array: " + Arrays.toString(result));
    }

    public static void merge(int[] arr1, int[] arr2, int[] result) {
        int i = 0, j = 0, k = 0;
        while (i < arr1.length && j < arr2.length) {
            if (arr1[i] < arr2[j]) {
                result[k++] = arr1[i++];
            } else {
                result[k++] = arr2[j++];
            }
        }
        while (i < arr1.length) {
            result[k++] = arr1[i++];
        }
        while (j < arr2.length) {
            result[k++] = arr2[j++];
        }
        Arrays.sort(result);
    }
}
