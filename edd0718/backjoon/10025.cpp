#include <iostream>
#include <queue>
using namespace std;
#define MAX 1000000

int main() {
    int n, k, g, x;
    int max=-1, min=MAX;
    vector<int> ice(MAX);
    std::cin >> n >> k;
    for (int i=0; i<n; i++) {
        std::cin >> g >> x;
        if (x>max) max = x;
        if (x<min) min = x;
        ice[x] = g;
    }
    queue<int> q;
    int sum = 0, answer = 0;
    for (int i=min; i<=max; i++) {
        if (q.size() <= 2*k+1) {
            q.push(ice[i]);
            sum += ice[i];
        }
        else {
            sum -= q.front();
            q.pop();
            q.push(ice[i]);
            sum += ice[i];
        }
        if (answer < sum) {
            answer = sum;
        }
    }
    std::cout << answer << std::endl;
    return 0;
}