package corejava;

public class findpalindrome {
	public static void main(String[] args) {
		String a = "bbxxxb";
		String c = longestPalindrome(a);
//		System.out.println(a.charAt(0)-'a'+1);
		System.out.println(c);
	}

	public static String longestPalindrome(String s) {
//		int[] arr = new int[32];
//
//		arr[s.charAt(0) - 'a' + 1] = s.charAt(0) - 'a' + 1;
//		int first = 0,last = 0;
//		for(int i=1;i<s.length();i++) {
//			int ch = s.charAt(i) - 'a' + 1;
//			if(ch == arr[ch] && arr[ch]>0) {
//				last= i;
////				System.out.println(last);
////				if(last+1-first+1 %2==0) {
////					return s.substring(first,last+1);
////				}
////				else {
////					return s.substring(first-1,last+1);
////				}
//				
//			}
//			first = i;
//			arr[ch] = s.charAt(i) - 'a' + 1;
//		}
//		return s.substring(first,last+1);
		
	    int n = s.length();
	    boolean[][] dp = new boolean[n][n];
	    String longest = "";
	    
	    // Base case: all substrings of length 1 are palindromes
	    for (int i = 0; i < n; i++) {
	        dp[i][i] = true;
	        longest = s.substring(i, i+1);
	    }
	    
	    // Check substrings of length 2 or more
	    for (int len = 2; len <= n; len++) {
	        for (int i = 0; i < n-len+1; i++) {
	            int j = i + len - 1;
	            if (s.charAt(i) == s.charAt(j)) {
	                if (len == 2 || dp[i+1][j-1]) {
	                    dp[i][j] = true;
	                    String sub = s.substring(i, j+1);
	                    if (sub.length() > longest.length()) {
	                        longest = sub;
	                    }
	                }
	            }
	        }
	    }
	    
	    return longest;

	}
}
