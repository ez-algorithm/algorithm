#include <iostream>
#include <stack>
#define REM 10007

int main() {
    int n;
    std::cin >> n;
    int dp[1000];
    dp[1]=1, dp[2]=2;

    for (int i=3; i<=n; i++) {
        dp[i] = (dp[i-2] + dp[i-1]) % REM;
    }

    std::cout << dp[n] << std::endl;
    return 0;
}