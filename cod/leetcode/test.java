package corejava;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class test {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int[] arr = {2,2,7,15};
		int target = 9;
		
		int[] arr1 = twoSum(arr,target);
		for (int i : arr1) {
			System.out.println(i);
		}
	}

	public static int[] twoSum(int[] nums, int target) {
		Map<Integer, Integer> map  = new HashMap<>();
		int[] arr = new int[2];
		
		for (int i = 0; i < nums.length; i++) {
			int value = target - nums[i];
			if(map.get(value) != null) {
				arr[0] = i;
				arr[1] = map.get(value)-1;
			}
			map.put(nums[i],i+1);
		}
		return arr;
	}

}
