package corejava;

import java.util.Arrays;

public class FindSoftarrays {
	public static double findMedianSortedArrays(int[] nums1, int[] nums2) {
		int len1= nums1.length,len2 = nums2.length;
        int[] nums = new int[len1+len2];
        merge(nums1, nums2, nums);
        int len = nums.length;
        double mergearr;
        System.out.println(len-1/2);
        if(len%2==0) {
        	
        	mergearr =(double)(nums[len/2] + nums[(len/2)-1]) / 2;
        }
        else {
        	mergearr = nums[(len-1)/2];
        }
        return mergearr;
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
        //sort after merge
        Arrays.sort(result);
    }
	public static void main(String[] args) {
		int[] nums1 = {1,2};
		int [] nums2 = {3,4};
		double a = findMedianSortedArrays(nums1, nums2);
		System.out.println(a);
	}
}
