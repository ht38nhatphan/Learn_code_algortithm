
#include <bits/stdc++.h>
#include <map>
#include <sstream>
#include <vector>
using namespace std;
int beauty(vector<int>& arr){
	int a = arr[0], b=arr[1], ma=arr[2], mb=arr[3];
    if(a < b){
        swap(a, b);
        swap(ma, mb);
    }
    if(ma == 0) return min(mb, b);
    if(mb == 0) return min(ma, a);
    if(a > (int)b * (int)ma) return min(a, ma * (b + 1)) + b;
    return a + b;
}
int main(){
	// long n;
	// F[0]=F[1]=1;
	// cin>>n;
	// cout << (n==0 ? 0 : f(n-1)) << endl;
	vector<int> a;
	for(int i=0;i<4;i++){
		int j;
		cin>>j;
		a.push_back(j);
	}
	int h = beauty(a);
	cout<<h;
	return 0;
}