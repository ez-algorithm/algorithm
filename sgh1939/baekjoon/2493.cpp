#include<bits/stdc++.h>
using namespace std;

struct Tower{
	int val;
	int idx;
	Tower(int a, int b){
		val = a;
		idx = b;
	}
};

int main(){
	stack<Tower> s;
	vector<int> result;
	int N,a;
	cin>>N;
	
	result.push_back(0);
	cin>>a;
	s.push(Tower(a, 1));
	
	for(int i=1; i<N; i++){
		// ют╥б	
		cin>>a;
		
		if(s.top().val >= a){
			result.push_back(s.top().idx);
			s.push(Tower(a, i+1));
		}else{
			while(!s.empty()){
				s.pop();
				if(s.empty()){
					result.push_back(0);
					s.push(Tower(a, i+1));
					break;
				}
				if(s.top().val >= a){
					result.push_back(s.top().idx);
					s.push(Tower(a, i+1));				
					break;	
				}
			}			
		}
	}
	
	for(int i=0; i<N; i++){
		cout<<result[i]<<" ";
	}

	return 0;
}
