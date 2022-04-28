#include <string>
#include <vector>
#include<bits/stdc++.h>

using namespace std;
int arr[1001] = {0,};
int dp(int n){
    if(arr[n] > 0) return arr[n];
    return arr[n] = dp(n-1) + n;
}

vector<int> calculate(int N, int cnt ){
    vector<int> result;
    vector<int> front_v[N];
    vector<int> back_v[N];
    int idx = 0, start = 1;
    int tmpN = N;
    
    
    while(tmpN > 0){
      if(start > cnt) break;
      
      for(int i=0; i<tmpN; i++){
         front_v[idx++].push_back(start++);
      }
      
      tmpN--;
      if(tmpN==0) break;
      
      idx--;
      for(int i=0; i<tmpN; i++){
         front_v[idx].push_back(start++);
      }
      tmpN--;
      if(tmpN==0) break;
      
      for(int i=0; i<tmpN; i++){
         back_v[--idx].push_back(start++);
      }
      tmpN--;
      //cout<<"N : "<<N<<endl;
      if(tmpN==0) break;
      
      idx++;
   }
    
    // reverse
    for(int i=0; i<N; i++){
      reverse(back_v[i].begin(), back_v[i].end());
   }
 
    // insert
    for(int i=0; i<N; i++){
      front_v[i].insert(front_v[i].end(), back_v[i].begin(), back_v[i].end());
   }
   
    // result
    for(int i=0; i<N; i++){
        for(int j=0; j<front_v[i].size(); j++){
            result.push_back(front_v[i][j]);
        }
    }

    return result;
}

vector<int> solution(int n) {
    vector<int> answer;
    arr[0] = 1;
   arr[1] = 1;
   arr[2] = 3;
    int cnt = dp(n);
    
    answer = calculate(n, cnt);
    return answer;
}
