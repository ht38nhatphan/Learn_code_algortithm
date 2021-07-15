// Đề bài:

// Có một con đường có độ dài n và 2 dãy bên con đường. Có tổng cộng 2*n mảnh đất có sẵn. Đối với mỗi mảnh đất có thể xây nhà hoặc là công ty nhưng phải thỏa mãn các điều kiện sau:

// Không có hai công ty nào là đối diện nhau
// Không có hai công ty nào là kề cạnh nhau
// Hãy tìm số cách để xây dựng từ những mảnh đất có sẵn. Vì đầu ra có thể rất lớn nên lấy dư cho 109 + 7
#include <bits/stdc++.h>
#define max 1000002
using namespace std;
unsigned long long dp[max];
long long countWays(long long n) {
		dp[max] = { 3 };
        if(n==1) return 3;
		dp[2] = 7;
		dp[3] = 17;
		for (int i = 4; i <= n; i++)
		{
			dp[i] = 2*dp[i - 1] + dp[i - 2];
			if (dp[i] > 1000000007)
			{
				dp[i] = dp[i] % 1000000007; 
			}
		}
		return dp[n];
}
int main(){
    int a;
    cin>>a;
    long long c = countWays(a);
    cout<<c;

    return 0;
}
