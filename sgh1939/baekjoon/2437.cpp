#include <bits/stdc++.h>
using namespace std;

int main() {
    int N;
    vector<int> v;
    
    cin >> N;
    for (int i = 0; i < N; i++) {
        int a;
        cin>>a;
        v.push_back(a);
    }
 
    sort(v.begin(), v.end());
    
    int res = 1;
    for (int i = 0; i < N; i++) {
        if (res < v[i]) {
            break;
        }
        res += v[i];
    }
 
 	// git
    cout << res;
}
