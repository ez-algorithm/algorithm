#include<bits/stdc++.h>
using namespace std;

int main(){
	int N, M, Max = -1, MaxVal = 0;
	vector<int> v;
	
	cin>>N>>M;
	for(int i=0; i<M; i++){
		int a;
		cin>>a;
		v.push_back(a);
	}
	
	sort(v.begin(), v.end(), greater<int>());
	
	int tmpM = 1;
	for(int i=0; i<M; i++){
		if((v[i] * tmpM) > Max) {
			if(tmpM > N) break;
			Max = v[i] * tmpM;
			MaxVal = v[i];
		}
		tmpM++;
	}

	cout<<MaxVal<<" "<<Max<<endl;
	return 0;
}
