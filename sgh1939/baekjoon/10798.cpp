#include <bits/stdc++.h>
using namespace std;

int main(){
   int arr[5][15] = {0,};

   for(int i=0; i<5; i++){
      for(int j=0; j<15; j++){
         arr[i][j] = 64;
      }
   }

   for(int i=0; i<5; i++){
      string s;
      getline(cin, s);
      for(int j=0; j<s.size(); j++){
         arr[i][j] = s[j];
      }
   }
   
   for(int i=0; i<15; i++){
      for(int j=0; j<5; j++){
         if(arr[j][i]== 64) continue;
         cout<<(char)arr[j][i];
      }
   } 
   
   return 0;
}

