
#include <map>
#include <iostream>
using namespace std;

#define long long long
const long M = 1000000007; // modulo
map<long, long> F;

long f(long n) {
	if (F.count(n)) return F[n];
	long k=n/2;
	if (n%2==0) { // n=2*k
		return F[n] = (f(k)*f(k) + f(k-1)*f(k-1)) % M;
	} else { // n=2*k+1
		return F[n] = (f(k)*f(k+1) + f(k-1)*f(k)) % M;
	}
}

main(){
	long n;
	F[0]=F[1]=1;
	while (cin >> n)
	cout << (n==0 ? 0 : f(n-1)) << endl;
}
// #include <bits/stdc++.h>
// using namespace std;

// #define long long long
// const int M = 1000000007;
// map<long, long> F;

// long f(long n) {
// 	if (F.count(n)) return F[n];
// 	long n1=n/2, n2=n-n1;
// 	return F[n] = (f(n1)*f(n2) + f(n1-1)*3*f(n2-1)) % M;
// }

// main() {
// 	F[0]=1; F[1]=2;
// 	for (int i=0; i<10; i++)
// 		cout << f(i) << endl;
// 	cout << f(1000000000000000000LL) << endl;
// }