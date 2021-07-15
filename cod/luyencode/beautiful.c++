#include <bits/stdc++.h>
using namespace std;
int daoso(int n){
    int tmp;
    int res = 0;
    while(n > 0){
        tmp = n % 10;
        res = res * 10 + tmp;
        n = n / 10;
    }
    return res;
}
bool beautiful(int c, int k){
    int h = daoso(c);
    int g = h-c;
    if(g<0){
        if ((-g%k==0) && (g<0)){
            return true;
        }
        
   }      
    else if (g>=0)
    {
       if ((g%k==0) && (g>=0)){
           return true;
       }
    }
    return false;
    
}
int number(int a,int b,int k){
    int dem=0;
    for(int i = a;i<=b;i++){
        if(beautiful(i,k)){
            dem++;
        }
    }
    return dem;
}

int main(){
    int a,b,c;
    cin>>a>>b>>c;
    int g = number(a,b,c);
    cout<<g;
    return 0;
}

