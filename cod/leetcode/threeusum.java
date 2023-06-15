package corejava;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.Comparator;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

public class threeusum {
	public static void main(String[] args) {
		int []nums = {0,3,0,1,1,-1,-5,-5,3,-3,-3,0};
		List<List<Integer>> arr = threeSum(nums);
		for(int i=0;i<arr.size();i++) {
			for(int j=0;j<3;j++) {
				System.out.println(arr.get(i).get(j) + " ");
				
			}
			
		}
	}
	
	
	public static List<List<Integer>> threeSum(int[] nums) {
		Arrays.sort(nums);
		int len = nums.length;
		Set<List<Integer>> arr = new HashSet<>();

		for(int i=0;i<len;i++) {
			for(int j=i+1;j<len-1;j++) {
				for(int g = j+1;g<len;g++) {
					
					int sum = nums[i] + nums[j]+nums[g];
					
					if(sum ==0) {
						arr.add(Arrays.asList(nums[i], nums[j], nums[g]));
					}}
				}
				
			}
		return new ArrayList<>(arr);
        
    }

	
	
	
}
