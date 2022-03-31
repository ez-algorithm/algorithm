#include <bits/stdc++.h>
using namespace std; 


// 첫번째 인덱스값을 구하고 뒤에서 하나씩 줄여가면서 찾아가기 
class Solution {
private : 
	string result = "";
    int min = 999999;
public:
    int searchFirst(string s, string t);
    int searchLast(string s, string t);
    bool isInside(string s, char target);
    string removeChar(string s, char target);
    bool checkInside(string s, string t);
    void Forward(string s, string t);
    void Reverse(string s, string t);
    
    
    string minWindow(string s, string t) {
    	
	    if(!checkInside(s, t)) return result;
		
		Forward(s,t);
		Reverse(s,t);
		
		return result;
    }
    
};

void Solution::Forward(string s, string t){
	while(s.size() > 0){
		if(!checkInside(s, t))break;
		
		string tmp = t;
		int first = searchFirst(s, tmp);
		
		tmp = removeChar(tmp, s[first]);
		int last = searchLast(s,tmp);
		if(last == -1){
			result = s[first];
			break;
		}
		string subString = s.substr(first, last-first+1);
		cout<<endl;
		cout<<"string : "<<s<<endl;
		cout<<"first : "<<first<<endl;
		cout<<"last : "<<last<<endl;
		cout<<"subString : "<<subString<<endl;
		
		if(checkInside(subString, t)){
			if(subString.size() < min){
				result = subString;
				min = subString.size();
			}
		}
		s = s.substr(first+1, s.size()-first+2);
	}
}

void Solution::Reverse(string s, string t){
	reverse(s.begin(), s.end());
	while(s.size() > 0){
		cout<<"reverse ==start"<<endl;
		if(!checkInside(s, t))break;
		
		string tmp = t;
		int first = searchFirst(s, tmp);
		
		tmp = removeChar(tmp, s[first]);
		int last = searchLast(s,tmp);
		if(last == -1){
			result = s[first];
			break;
		}
		string subString = s.substr(first, last-first+1);
		cout<<endl;
		cout<<"string : "<<s<<endl;
		cout<<"first : "<<first<<endl;
		cout<<"last : "<<last<<endl;
		cout<<"subString : "<<subString<<endl;
		
		if(checkInside(subString, t)){
			if(subString.size() < min){
				reverse(subString.begin(), subString.end());
				result = subString;
				reverse(subString.begin(), subString.end());
				min = subString.size();
			}
		}
		s = s.substr(first+1, s.size()-first+2);
				cout<<"reverse ==end"<<endl;
	}	
}


int Solution::searchFirst(string s, string t){
   int result = 999999;
   for(int i=0; i<t.size(); i++){
      int tmp = s.find(t[i]);
      if(tmp == string::npos) continue;
      if(tmp < result) result = tmp;
   }
   return result;
}

int Solution::searchLast(string s, string t){
   int result = -1;
   for(int i=0; i<t.size(); i++){
      int tmp = s.rfind(t[i]);
      if(tmp == string::npos) continue;
      if(tmp > result) result = tmp;
   }
   return result;
}

bool Solution::isInside(string s, char target){
	int tmp = s.find(target);
	if(tmp == string::npos) return false;
	else return true;    
}

string Solution::removeChar(string s, char target){
	s.erase(find(s.begin(), s.end(), target));
	return s;    
}

bool Solution::checkInside(string s, string t){
	for(int i=0; i<t.size(); i++){
		if(isInside(s, t[i])){
			s = removeChar(s, t[i]);
		}else return false;
	}
	return true;    
}

int main(){
	string a,b;
    cin>>a>>b;
	Solution sol;
	string result = sol.minWindow(a,b);	
	cout<<"결과 : "<<result<<"\n";
}
