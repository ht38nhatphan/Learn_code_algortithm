#include <bits/stdc++.h>
using namespace std;
#define ll long long

int main(){
    int n,m,k;
    cin>>n>>m;
    ll c = modulo_combination(m,n,k);
    cout<<c;
    return 0;
}
