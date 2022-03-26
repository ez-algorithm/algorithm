#include <iostream>

#define MAX 100

void dp() {
    int n;
    long long P[MAX];
    std::cin >> n;

    P[1] = P[2] = P[3] = 1;
    for (int i=4; i<=n; i++) {
        P[i] = P[i-2] + P[i-3];
    }
    std::cout << P[n] << std::endl;
}

int main() {
    int t; // testcase
    std::cin >> t;
    for (int i=0; i<t; i++) {
        dp();
    }
}