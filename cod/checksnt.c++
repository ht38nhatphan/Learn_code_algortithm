#include <bits/stdc++.h>
using namespace std;
#define ll long long
// int checksnt(int a,int i,int n){
//     if(n<i){
//         return 1;
//     }
//     if(a%i==0){
//         return 0;
//     }
//     return checksnt(a,i+1,n);
// }
bool checksnt1(int a){
    if(a<2){
        return false;
    }
    for(int i=2;i<=sqrt(a);i++){
        if(a%i==0){
            return false;
        }
    }
    return true;
}
int main(){
    // ll n;
    // cin>>n;
    // for(int i =2;i<=n;i++){
    //     if(checksnt(i,2,sqrt(i))==1){
    //     cout<<"YES"<<' ';
    // }
    // else{
    //     cout<<"NO"<<' ';
    // }
    // }
    int n;
    cin>>n;
    if(checksnt1(n)){
        cout<<"YES";
    }
    else{
        cout<<"NO";
    }
    return 0;
}