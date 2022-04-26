#include<bits/stdc++.h>
using namespace std;

char puyo[12][6]={0,};
int Visit[12][6]={0,};

// 방향 
int dx[4] = {0, 1, 0, -1};
int dy[4] = {1, 0, -1, 0};

// 연결 된 색상의 좌표값들 
vector<pair<int, int>> relayPoint;

// 4개 이상 연결된 좌표값들을 담은 vector 
vector<vector<pair<int, int>>> removePoint;
int result;


// dfs 탐색 
void dfs(int x, int y){
   Visit[x][y] = 1;
   for(int i=0; i<4;i++){
      int xx = x + dx[i];
      int yy = y + dy[i];
      if(xx >=0 && xx <= 11 && yy >=0 && yy <= 5 && puyo[xx][yy] == puyo[x][y] && Visit[xx][yy]==0){
         relayPoint.push_back(make_pair(xx, yy));
         dfs(xx, yy);
      }
   }
}

// 중력! 
void gravity(){
   for(int i=0; i<6; i++){
      for(int j=11; j>=0; j--){
         if(puyo[j][i]=='.'){
            for(int n=j-1; n>=0; n--){
               if(puyo[n][i]!='.'){
                  puyo[j][i] = puyo[n][i];
                  puyo[n][i] = '.';
                  break;
               }
            }
         }
      }
   }

}

void Input(){
    for (int i = 0; i < 12; i++)
        for (int j = 0; j < 6; j++)
            cin>>puyo[i][j];
}

// 4개 이상 펑! 
bool remove(){
   if(removePoint.empty()) return false;
   for(auto it : removePoint){
      for(long unsigned int i=0; i<it.size(); i++){
         int x = it[i].first;
         int y = it[i].second;
         puyo[x][y] = '.';
      }
   }
   removePoint.clear();
   gravity();
   result++;
   return true;
}
 
void gameStart(){
   for(int i=0; i<12; i++){
      for(int j=0; j<6; j++){
         if(puyo[i][j]== '.') continue;
         if(Visit[i][j]==0){
            relayPoint.push_back(make_pair(i,j));
            dfs(i, j);
            if(relayPoint.size() > 3 ) {
               removePoint.push_back(relayPoint);
               relayPoint.clear();
            }else relayPoint.clear();
         }
      }
   }
}

int main(){
   Input();
   gameStart();
   while(remove()){
      memset(Visit, 0, sizeof(Visit));
      gameStart();
   }
   
   cout<<result;
   
   return 0;
}
