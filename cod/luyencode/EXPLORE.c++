//EXPLORE - Kỳ nghỉ của Bessie
/*
Đề bài
Bessie đang dạo chơi trên 1 con đường với những thắng cảnh hấp dẫn. Con đường có thể được coi như 1 trục tọa độ, với vị trí trại của Bessie nằm tại x = 0x=0, và các thắng cảnh nằm tại vị trí x_1, x_2, \ldots, x_nx 
1
​
 ,x 
2
​
 ,…,x 
n
​
 . Bessie muốn thăm quan càng nhiều thắng cảnh càng tốt, nhưng cô chỉ có tối đa TT phút, sau đó đêm sẽ đến và cô không thể nhìn thấy gì cả.

Thêm vào đó, thứ tự thăm quan các thắng cảnh cũng bị ràng buộc. Theo đó, cô sẽ thăm quan các thắng cảnh lần lượt theo khoảng cách của nó đến trại của Bessie (tất cả các khoảng cách này là đôi một phân biệt). Thời gian để Bessie di chuyển 1 đơn vị trên trục tọa độ là 1 phút, thời gian thăm quan 1 thắng cảnh là không đáng kể.

Hãy giúp Bessie tính số lượng thắng cảnh tối đa mà cô có thể thăm quan.
25 5
10
-3
8
-7
1


Output #1

4*/
#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
using namespace std;
void bubble(int a[],int b[],int n)
{
    for(int i=0;i<n-1;i++)
        for(int j=n-1;j>i;j--)
    {
        if(a[j]<a[j-1]){
            swap(a[j],a[j-1]);
            swap(b[j],b[j-1]);}
    }
}
int abs(int n)
{
    if(n>=0) return n;
    else return -n;
}
void quick(int a[],int b[], int l, int r)
{
	srand(time(NULL));
	int key = a[l + rand() % (r-l+1)];
	//int key = a[(l+r)/2];
	int i = l, j = r;

	while(i <= j)
	{
		while(a[i] < key) i++;
		while(a[j] > key) j--;
		if(i <= j)
		{
			if (i < j)
				{
				    swap(a[i],a[j]);
                    swap(b[i],b[j]);
				}
			i++;
			j--;
		}
	}
	if (l < j) quick(a,b, l, j);
	if (i < r) quick(a,b, i, r);
}
int x[200001],y[200001];
int main()
{
    int n,t;
    cin>>t>>n;
    for(int i=0;i<n;i++)
    {
        cin>>x[i];
    }
    for(int i=0;i<n;i++)
    {
        y[i]=abs(x[i]);
    }
    quick(y,x,0,n-1);
    int time=x[0];
    int dem=0;
    while(time<=t)
    {
        time+=abs(x[dem]-x[dem+1]);
        dem++;
    }
    cout<<dem<<endl;
}