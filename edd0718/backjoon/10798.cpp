// boj 10798 - 세로읽기
#include <iostream>
#include <string>
#include <vector>
using namespace std;

int main() {
   vector<string> toy(5);
    for (int i=0; i<5; i++) {
        std::cin >> toy[i];
    }

    for (int i=0; i<15; i++) {
        for (int j=0; j<5; j++) {
            if (i<toy[j].size()) {
                std::cout << toy[j][i];
            }

        }
    }

    return 0;
}