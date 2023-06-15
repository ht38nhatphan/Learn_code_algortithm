package corejava;

import java.util.ArrayList;
import java.util.List;

public class Q1 {

	public static void main(String[] args) {
		int n=4;
		System.out.println(Fv(n));
	}
	public static int Fv(int n) {
		List<Integer> arr = new ArrayList<Integer>();
		arr.add(4);
		arr.add(7);
		arr.add(5);
		if(n<=3) {
			return arr.get(n);
		}
		else {
			for(int i=3;i<=n;i++) {
				arr.add(arr.get(i-3)+arr.get(i-2)+arr.get(i-1));
			}
		}
		return arr.get(n);
	}
}
