// Cho một dãy arr gồm các bài hát. Đối với từng bài hát sẽ có các thời gian phát nhạc khác nhau. Khi biểu diễn người nhạc sĩ muốn chọn các cặp bài hát sao cho các cặp này đều chia hết cho time. Hãy tìm các cặp bài hát, tương ứng với việc tìm các cặp i, j sao cho i < j và arr[i] + arr[j] % time = 0. 

// Ví dụ:

// Với arr = [30,20,150,100,40], time = 60. Đầu ra pairsOfSongs(arr) = 3.
//       Giải thích: Các cặp thỏa mãn là (0, 2), (1, 3), (1, 4)

// Đầu vào/Đầu ra:

// [Thời gian chạy] 0.1s với C++, 0.6s với Java và C#, 0.8s với Python, Go và JavaScript.
// [Đầu vào] Array of integer arr.
//       2 <= arr.size() <= 10000

//       1 <= arr[i] <= 10^9

// [Đầu ra] Integer 
//      Số lượng cặp thỏa mãn yêu cầu đề bài
#include <bits/stdc++.h>
using namespace std;
int pairsOfSongs(vector<int> arr, int time)
{
    int n = arr.size(), result = 0;
        unordered_map<int, int> mp;
        mp.clear();
        for(int i : arr)
        {
            mp[i % time]++;
        }
        for(auto i : mp)
        {
            int key = (time - i.first) % time;
            if(mp.find(key) != mp.end())
            {
                if(i.first == key)
                    result += i.second * (i.second - 1);
                else 
                    result += i.second * mp[key];
            }
        }
		// Divide the result by 2 because the one pair is counted twice, 
		// firstly as i,j and secondly as j,i (i < j),
		// as we are not keeping track of the indices of the ith time
        return (result / 2); 
}
int main() {
    vector<int> arr = {30,20,150,100,40};
    int time = 3;
    int c =  pairsOfSongs(arr,time);
    cout<<(c);
}