import java.util.*;
import java.lang.*;

class Main
{
	static final int MOD = 1000000007;
	public static void main (String[] args) throws java.lang.Exception
	{
		 Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int k = sc.nextInt();
        int[][] matrix = new int[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                matrix[i][j] = sc.nextInt();
            }
        }
        int[][] dp = new int[n][n];
        for (int i = 0; i < n; i++) {
            dp[i][0] = 1;
        }
        for (int j = 0; j < n; j++) {
            dp[0][j] = 1;
        }
        for (int i = 1; i < n; i++) {
            for (int j = 1; j < n; j++) {
                dp[i][j] = ((matrix[i][j] * dp[i][j-1]) % MOD
                            + (matrix[i][j] * dp[i-1][j]) % MOD
                            - (matrix[i][j] * dp[i-1][j-1]) % MOD
                            + dp[i-1][j-1]) % MOD;
            }
        }
        System.out.println(dp[n-1][n-1]);
	}
}