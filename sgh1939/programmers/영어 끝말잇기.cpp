#include<bits/stdc++.h>
using namespace std;

vector<int> solution(int n, vector<string> words) {
    vector<int> answer;
    
    // 단어 저장소 
    vector<string> record;

   // 제일 처음 단어의 첫번째 값 
    char last = words[0][0];
   
   // 사람 순번 
   int human = 1;
   
   // 게임 횟수 
   int turn = 1;
   
   // 단어 수 
   int check = 0;
    
    for(int i=0; i<words.size(); i++){
       auto it = find(record.begin(), record.end(), words[i]);
       
      // 만약 안 나왔던  단어라면 
      if(it == record.end()){
          
          // 단어 저장소에 저장 
          record.push_back(words[i]);

         // 제일 단어의 제일 첫 알파벳을 가져옴 
         char first = words[i][0];
          
          // 이전 마지막 단어와 첫 번째 단어가 일치하지 않으면 break; 
          if(last != first )break;
          
          // 마지막 단어 값 갱신 
         last = words[i][words[i].length()-1];
         
         // 다음 사람 
         human++;
         
         // 다음 단어  
         check++;
         
         // 사람 다 돌았으면 turn++ 
         if( human > n){
            turn++;
            human = 1;
         }
         
      }else break;
   }
   
   if( words.size() == check){
      answer.push_back(0);
      answer.push_back(0);      
   }else{
      answer.push_back(human);
      answer.push_back(turn);
   }
 
    return answer;
}
