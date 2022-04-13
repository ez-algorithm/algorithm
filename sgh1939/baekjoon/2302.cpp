#include <bits/stdc++.h>
using namespace std;

long long arr[41] = { 0, };
long long dp(int n) {
	if (n == 1) return 1;
	if (n == 2) return 2;
	if (arr[n] != 0) return arr[n];

	return arr[n] = dp(n - 1) + dp(n - 2);
}

int main() {
	vector<int> v;
	int N, M, a, start = 0;
	arr[0] = 1;

	cin >> N >> M;

	for (int i = 0; i < M; i++) {
		int tmp = 0;
		cin >> a;
		tmp = a - start - 1;
		v.push_back(tmp);
		start = a;
	}
	v.push_back(N - start);

	long long result = dp(v[0]);

	for (int i = 1; i < v.size(); i++) {
		result *= dp(v[i]);
	}

	cout << result;

	return 0;
}
