#include <bits/stdc++.h>
using namespace std;
vector<int> v;
// �� �׽�Ʈ ���̽��� ������� ���� ���� 
int total_num = 0;

void DFS(int N, int sum){
   if(sum > N) return;
   if(N == sum){
      total_num++;
      return;
   }else{
      for(int i=1; i<=3; i++){
         DFS(N, sum + i);
      }
   }
}

int main(){
   int T;
   cin>>T;
   
   for(int i=0; i<T; i++){
      int tmp;
      cin>>tmp;
      DFS(tmp, 0);
      v.push_back(total_num);
      total_num = 0;
   }
   
   for(int i=0; i<T; i++)
      cout<<v[i]<<"\n";
   
   return 0;
}

