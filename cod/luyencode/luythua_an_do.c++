#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;
#define ll long long
ll mod = 1000000007;
ll luythua(ll a,ll n){
    if (n == 0){
        return 1;
    } 
    ll t = luythua(a, n / 2);
    t = (t * t) % mod; 
    if (n % 2 == 1){
        t = (t * a) % mod;
    } 
    return t;
}

int32_t main() {
    long long a,n;
    cin>>a>>n;
    long long c = luythua(a,n);
    cout<<c;

}

