#include <iostream>
#include <vector>
#include <algorithm>
#define INF 2000000000
using namespace std;

int main() {
    int n, trg, res;
    std::cin >> n;
    vector<int> num(n);
    for (int i=0; i<n; i++) {
        std::cin >> num[i];
    }
    std::cin >> trg;
    sort(num.begin(), num.end());
    vector<int> ans(3);
    
    int start = 0;
    int end = n-1;
    int key = start+1;
    int close = INF;
    while (start < end && key < end) {
        int sum = num[start] + num[key] + num[end];
        if (sum != trg) {
            if (abs(sum-trg) < close) {
                close = abs(sum-trg);
                ans[0] = num[start];
                ans[1] = num[key];
                ans[2] = num[end];
            }
            if (key == end-1) {
                start++;
                key = start;
            }
            key++;
        }
        else {
            ans[0] = num[start];
            ans[1] = num[key];
            ans[2] = num[end];
            break;
        }
    }
    res = ans[0]+ans[1]+ans[2];
    std::cout << res << std::endl;
    return 0;
}