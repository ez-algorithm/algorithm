#include <iostream>
#include <vector>
using namespace std;
#define MAX 40

int main() {
    int n, m;
    int answer = 1;
    std::cin >> n;
    std::cin >> m;
    vector<int> DP(MAX);
    vector<int> VIP(MAX);
    for (int i=0; i<m; i++) {
        std::cin >> VIP[i];
    }
    // vip x -> 경우의 수
    DP[1]=1, DP[2]=2;
    for (int i=3; i<=n; i++) {
        DP[i] = DP[i-2] + DP[i-1];
    }
    // vip o -> 경우의 수 (누적곱)
    int key=0;
    for (int i=0; i<m; i++) {
        answer *= DP[VIP[i] - key - 1];
        key = VIP[i];
    }
    answer *= DP[n-key];
    std::cout << answer << std::endl;
    return 0;
}