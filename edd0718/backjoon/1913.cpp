// boj 1913 - 달팽이
#include <iostream>
using namespace std;

int main() {
    int x = 0, y = 0;
    int key = 1;
    int n, m, idx, idy;
    std::cin >> n;
    std::cin >> m;
    int num = n*n;
    int D[n][n];
    for (int i=0; i<n; i++) {
        for (int j=0; j<n; j++) {
            D[i][j] = 0;
        }
    }
    
    for (int k=0; k<n; k++) {
        D[x][y] = num--;
        x += key;
    }
    x -= 1;
    for (int i=n-1; i>0; i--) {
        for (int j=0; j<i; j++) {
            y += key;
            D[x][y] = num--;
        }
        key *= -1;
        for (int k=0; k<i; k++) {
            x += key;
            D[x][y] = num--;
        }
    }

    for (int i=0; i<n; i++) {
        for (int j=0; j<n; j++) {
            if (D[i][j] == m) {
                idx = i+1;
                idy = j+1;
            }
            std::cout << D[i][j] << ' ';
        }
        std::cout << std::endl;
    }
    std::cout << idx << ' ' << idy << std::endl;
    return 0;
}