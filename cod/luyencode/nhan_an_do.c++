#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;
#define ll long long
ll mod = 1000000007;
/*Thuật toán đơn giản như sau: để tính 
a
∗
b
 ta sẽ tính

a
∗
b
2
+
a
∗
b
2
 nếu b chẵn
a
∗
b
2
+
a
∗
b
2
+
a
 nếu b lẻ*/
ll nhan(ll a,ll n){
    if (n == 0){
        return;
    } 
    ll t = nhan(a, n / 2);
    t = (t + t) % mod; 
    if (n % 2 == 1){
        t = (t + a) % mod;
    } 
    return t;
}

int32_t main() {
    long long a,n;
    cin>>a>>n;
    long long c = nhan(a,n);
    cout<<c;

}

