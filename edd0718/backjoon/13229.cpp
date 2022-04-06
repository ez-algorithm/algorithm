// boj 13229 - Selection Sum
#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n, m, start, end;
    std::cin >> n;
    vector<int> a(n);
    for (int i=0; i<n; i++) {
        std::cin >> a[i];
    }
    std::cin >> m;
    for (int i=0; i<m; i++){
        std::cin >> start >> end;
        int sum=0;
        for (int j=start; j<=end; j++) {
            sum += a[j];
        }
        std::cout << sum << std::endl;
    }
    return 0;
}