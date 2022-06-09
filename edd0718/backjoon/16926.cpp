#include <iostream>
#include <algorithm>
using namespace std;

int arr[301][301];
int n, m, r;

void dfs(int rt) {
    if (rt == 0) return;
    //int cnt = min(n,m) / 2;
    int cnt = rt % ((n-1)*2) + ((m-1)*2);
    for (int start=0; start<cnt; start++) {
        int r = start;
        int c = start;
        int ans = arr[r][c];
        // left top -> left bottom
        while (r < n-1-start) {
            int nVal = arr[r+1][c];
            arr[r+1][c] = ans;
            ans = nVal;
            r++;
        }
        // left bottom -> right bottom
        while (c < m-1-start) {
            int nVal = arr[r][c+1];
            arr[r][c+1] = ans;
            ans = nVal;
            c++;
        }
        // right bottom -> right top
        while (r >= start+1) {
            int nVal = arr[r-1][c];
            arr[r-1][c] = ans;
            ans = nVal;
            r--;
        }
        // right top -> left top
        while (c >= start+1) {
            int nVal = arr[r][c-1];
            arr[r][c-1] = ans;
            ans = nVal;
            c--;
        }

    }
    dfs(rt-1);
}

int main() {
    std::cin >> n >> m >> r;
    
    for (int i=0; i<n; i++) {
        for (int j=0; j<m; j++) {
            std::cin >> arr[i][j];
        }
    }
    dfs(r);
    for (int i=0; i<n; i++) {
        for (int j=0; j<m; j++) {
            std::cout << arr[i][j] << " ";
        }
        std::cout << std::endl;
    }
    return 0;
}