package corejava;

public class Atoi {
	public static void main(String[] args) {
		String a = "2147483646";
		int i = myAtoi(a);
//		int j = Integer.parseInt(a);
		System.out.println(i);
	}
	public static int myAtoi(String s) {
		  if (s == null || s.isEmpty()) {
		        return 0;
		    }

		    int sign = 1, i = 0, n = s.length(), result = 0;
		    while (i < n && Character.isWhitespace(s.charAt(i))) {
		        i++;
		    }

		    if (i < n && (s.charAt(i) == '+' || s.charAt(i) == '-')) {
		        sign = (s.charAt(i++) == '-') ? -1 : 1;
		    }

		    while (i < n && Character.isDigit(s.charAt(i))) {
		        int digit = s.charAt(i++) - '0';
		        if (result > Integer.MAX_VALUE / 10 || (result == Integer.MAX_VALUE / 10 && digit > Integer.MAX_VALUE % 10)) {
		            return (sign == -1) ? Integer.MIN_VALUE : Integer.MAX_VALUE;
		        }
		        result = result * 10 + digit;
		    }

		    return sign & result;
    }
}
