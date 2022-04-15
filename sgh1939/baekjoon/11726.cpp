#include <bits/stdc++.h>
using namespace std;

long long arr[1001] = {0,};
long long dp(int n){
	if(n == 0) return 1;
	if(n == 1) return 1;
	if(n == 2) return 2;
	if(arr[n] != 0) return arr[n];
	
	return arr[n] = (dp(n-1) + dp(n-2))%10007;
}

int main(){
	int n;
	cin>>n;
	
	cout<<dp(n);
	
	return 0;
}
