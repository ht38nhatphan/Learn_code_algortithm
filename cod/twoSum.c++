#include <bits/stdc++.h>
#include <vector>
#include <unordered_map>
using namespace std;

vector<int> twoSum(vector<int>& nums, int target) {
    unordered_map<int,int>map;
vector<int>v;
    for(int i=0;i<nums.size();i++)
    {
          
            
           
            int a = target-nums[i];   //  Let's  nums = [2,7,11,15], target = 9, then a=9-2;   so a=7;
			     if(map[a])           //  If map[7], i mean if there is something on 7th index in map, it means 7 is present so 
				                         // we get the answer (2,7) 
              {
                  v.push_back(i);
                  v.push_back(map[a]-1);
                  break;
              }
              map[nums[i]] = i+1; // Here i'm inserting (i+1) not (i) because if i==0, then above if condition will never read
            
    }
      
   return v; 
}
int main(){
    vector<int> a = {21,71,11,8,7,2};
    int b = 9;
    vector<int>c = twoSum(a,b);
    for(int i : c){
        cout<<i <<' ';
    }
    return 0;
}