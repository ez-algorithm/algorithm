#include<bits/stdc++.h>
using namespace std;

vector<int> solution(int n, vector<string> words) {
    vector<int> answer;
    
    // �ܾ� ����� 
    vector<string> record;

   // ���� ó�� �ܾ��� ù��° �� 
    char last = words[0][0];
   
   // ��� ���� 
   int human = 1;
   
   // ���� Ƚ�� 
   int turn = 1;
   
   // �ܾ� �� 
   int check = 0;
    
    for(int i=0; i<words.size(); i++){
       auto it = find(record.begin(), record.end(), words[i]);
       
      // ���� �� ���Դ�  �ܾ��� 
      if(it == record.end()){
          
          // �ܾ� ����ҿ� ���� 
          record.push_back(words[i]);

         // ���� �ܾ��� ���� ù ���ĺ��� ������ 
         char first = words[i][0];
          
          // ���� ������ �ܾ�� ù ��° �ܾ ��ġ���� ������ break; 
          if(last != first )break;
          
          // ������ �ܾ� �� ���� 
         last = words[i][words[i].length()-1];
         
         // ���� ��� 
         human++;
         
         // ���� �ܾ�  
         check++;
         
         // ��� �� �������� turn++ 
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
