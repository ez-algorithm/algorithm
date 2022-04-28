// boj 9096 - 1,2,3 더하기
#include <iostream>
#define MAX 11

void DP() {
    int P[MAX], n;
    std::cin >> n;
    P[1]=1, P[2]=2, P[3]=4;
    for (int i=4; i<=n; i++) {
        P[i] = P[i-1] + P[i-2] + P[i-3];
    }
    std::cout << P[n] << std::endl;
}

int main() {
    int tc;
    std::cin >> tc;
    for (int i=0; i<tc; i++) {
        DP();
    }
    return 0;
}