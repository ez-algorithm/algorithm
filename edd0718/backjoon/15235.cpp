#include <iostream>
#include <queue>
#include <vector>
using namespace std;

int main(void) {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    queue<pair<int, int>> q;
    int N = 0; 
    int total = 0;
    cin >> N;
    // 특정 인덱스에 해당하는 사람의 피자 분배 완료
    vector<int> v(N);
    for (int i=0; i<N; i++) {
        int pizza;
        cin >> pizza;
        total += pizza;
        q.push(make_pair(pizza, i));
    }
    for (int i=1; i<total+1; i++) {
        // 피자 개수가 1보다 크면
        if (q.front().first > 1) {
            // 각각의 원하는 피자 개수 - 1
            q.push(make_pair(q.front().first - 1, q.front().second));
        }
        // 피자 분배 완료되는 인덱스
        else {
            v[q.front().second] = i;
        }
        q.pop();
    }
    for (int i=0; i<N; i++) {
        cout << v[i] << ' ';
    }
    printf("\n");
}
