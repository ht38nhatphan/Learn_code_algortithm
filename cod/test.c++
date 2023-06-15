#include <bits/stdc++.h>
#include <map>
#include <sstream>
#include <vector>
#include <regex>
using namespace std;
// #define int a[4][4],b[4][4];
// for string delimiter
int res[4];

void split (string s, string delimiter) {
    size_t pos_start = 0, pos_end, delim_len = delimiter.length();
    string token;
	int i =0;
    while ((pos_end = s.find (delimiter, pos_start)) != string::npos) {
        token = s.substr (pos_start, pos_end - pos_start);
        pos_start = pos_end + delim_len;
        res[i] = atoi(token.c_str());
		i++;
    }
	token = s.substr (pos_start);
    res[3] = atoi(token.c_str());
}
int arr1[4][4] = {{1,1,1,1},{1,0,0,1},{1,0,0,1},{1,1,1,1}};
int arr[4][4];

std::vector<int> as (){
	int max =0;
	int h=0,k=0;
	std::vector<int>a ;
	arr1[4][4];
	for(int i = 0;i<4;i++){
			for(int j=0;j<4;j++){
				if(arr1[i][j]==1){
					if(arr[i][j]>=max){
						max = arr[i][j];
						// luu[0] = i;
						// luu[1] = j;
						k = i;
						h = j;
					}
					// else if(max[0]==arr[i][j]){
					// 	k = i;
					// 	h = j;
					// }
					
				}
			}
		}
		a.push_back(k);
		a.push_back(h);
		a.push_back(max);
	return a;
}
int maxDiff(std::vector<string> board)
{
	
	int luu[2]={0,0};
	int luusum[2] = {0,0};
	std::vector<int>max;
	
	for(int i=0;i<4;i++){
		split(board[i]," ");
		for(int j=0;j<4;j++){
			arr[i][j] = res[j];
		}
	}
	
	//người a hay b
	int c=0;
	int k=0,h=0,c1=10;
	while(luusum[0]+luusum[1]<=94){
		
		//di rôi ko di lai
		max = as();
		
		k = max[0];
		h = max[1];
		arr1[k][h] = -1;
		if(k==0 && h<3&& h!=0){
			if(arr1[k][h+1] ==0){
				if(arr[k][h]>arr[k][h+1]){
					arr1[k][h+1] = 1;
				}
				else{
					arr1[k][h+1] =0;
					max = as();
					k = max[0];
					h = max[1];
				}
				
			}
		}
		if(k==1 && h<=2){
			if(arr1[k][h+1]==0){
				if(arr[k][h]>arr[k][h+1]){
					arr1[k][h+1]=1;
				}
				else{
					arr1[k][h+1] =0;
					max = as();
					k = max[0];
					h = max[1];
				}
			}
			if(arr1[k+1][h]==0){
				if(arr[k][h]>arr[k+1][h]){
					arr1[k+1][h]=1;
				}
				else{
					arr1[k+1][h]=0;
					max = as();
					k = max[0];
					h = max[1];
				}
				
			}
		}
	if(k>0&&h>2){
		if(arr1[k-1][h]==0){
			if(arr[k][h]>arr[k-1][h]){
				arr1[k-1][h]=1;
			}
			else{
				arr1[k-1][h]=0;
				max = as();
					k = max[0];
					h = max[1];
			}
			
		}
		if(arr1[k][h-1]==0){
			if(arr[k][h]>arr[k][h-1]){
				arr1[k][h-1]=1;

			}
			else{
				arr1[k][h-1]=0;
					max = as();
					k = max[0];
					h = max[1];
			}
		}
	}
		if(h==3){
			if(arr1[k][h-1]==0){
				if(arr[k][h]>arr[k][h-1]){
					arr1[k][h-1]=1;
				}
				else{arr1[k][h-1]=0;
				max = as();
					k = max[0];
					h = max[1];
				}
				
		}
	}
	if(h==0&&k>=3&&h!=0){
		if(arr1[k][h+1]==0){
			if(arr[k][k]>arr[k][k+1]){
				arr1[k][k+1]=1;
			}
			else{
			arr1[k][h+1]=1;
			max = as();
					k = max[0];
					h = max[1];
			}
			
		}
		
	}
	if(k==3){
		if(arr1[k-1][h]==0){
			if(arr[k][h]>arr[k-1][h]){
				arr1[k-1][h] =1;
			}
			else{
				arr1[k-1][h] =0;
				max = as();
					k = max[0];
					h = max[1];
			}
			
		}
		
	}
	if(k==2&&h<3){
		if(arr1[k][h+1]==0){
			if(arr[k][h+1]){
				arr1[k][h+1]=1;
			}
			else{
				arr1[k][h+1]=0;
				max = as();
					k = max[0];
					h = max[1];
			}
		}
		if(arr1[k+1][h]==0){
			if(arr[k][h]>arr[k+1][h]){
				arr1[k+1][h]==1;
			}
			else{
			arr1[k+1][h]=1;
			max = as();
					k = max[0];
					h = max[1];
			}
		}
		
	}
	if(c==0){
			luusum[0]+=max[2];
		}
		else if(c==1){
			luusum[1]+=max[2];
		}
		c= c==0?c=1:0;
	}
	
	return luusum[0] - luusum[1];
	
}

int main() {
    vector<string> board;
	board = {"12 4 5 13", "3 14 16 9",  "11 6 15 8",  "2 1 7 10"};
	int c = maxDiff(board);
	cout<<c;

    return 0;
}

	

