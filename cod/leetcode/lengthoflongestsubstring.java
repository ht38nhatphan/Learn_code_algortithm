package corejava;

import java.util.HashSet;
import java.util.Set;

public class lengthoflongestsubstring {
	public static void main(String[] args) {
		String a = "abcacbzedd";
		int len = lengthOfLongestSubstring(a);
		System.out.println(len);
	}

	public static int lengthOfLongestSubstring(String s) {
//		Set<String> set = new HashSet<String>();
//		int dem = 0,tong = 0;
//		for(int i = 0;i<s.length();i++) {
//			for(int j = i;j<s.length() && set.contains(String.valueOf(s.charAt(j)))==false ;j++) {
////				if(j==s.length()-1) {
////					return tong;
////				}
//				dem++;
//				set.add(String.valueOf(s.charAt(j)));
//				
//			}
//			if(tong<dem) {
//				tong =dem;
//			}
//			dem = 0;
//			set.clear();
////			set.add(String.valueOf(s.charAt(i)));
//		}
//		return tong;
		  int ans=0;
	        int n=s.length();
	        int win =0;
	        int[] idx =new int[96];
	        for(int i=0;i<n;i++)
	        {
	            int c=s.charAt(i)-32;
	            win=Math.max(idx[c],win);
	            ans=Math.max(ans,i-win+1);
	            idx[c]=i+1;
	        }
	        return ans;
	}
}
