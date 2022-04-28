#include <bits/stdc++.h>
using namespace std;
vector<long long> v;

void initialize(){
   v={1,1,1,2,2};
   long long tmp;
   long long start = 0, end = 4;
   for(int i=5; i<=100; i++){
      tmp = v[start] + v[end];
      v.push_back(tmp);
      start++;
      end++;
      tmp=0;
   }
}

int main(){
   initialize();
   int T,a;
   cin>>T;
   
   for(int i=0; i<T; i++){
      cin>>a;
      cout<<v[a-1]<<"\n";
   }

   return 0;
}

