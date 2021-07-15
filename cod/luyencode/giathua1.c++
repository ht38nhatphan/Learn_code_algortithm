#include <bits/stdc++.h>
using namespace std;
int gt(int n)
{
    int gt = 1;
    for (int i = 2; i <= n; i++)
    {
        gt *= i;
    }
    return gt;
}

int main()
{
    double x, S = 0.0;
    int n;
    cin >> x >> n;
    for (int i = 1; i <= n; i++)
    {
        S += (pow(x, i) / gt(i));
    }
    cout<<fixed<<setprecision(2)<<S;
    return 0;
}