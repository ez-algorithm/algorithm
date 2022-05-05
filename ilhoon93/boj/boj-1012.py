# 유기농배추
import pprint

def dfs(i, j):
    visited[i][j] = True
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for d in range(4):
        ni = i + dx[d]
        nj = j + dy[d]
        
        if ni < 0 or ni >= n or nj < 0 or nj >= m:
            continue
        
        if data[ni][nj] == 1:
            if visited[ni][nj] == False:
                dfs(ni, nj)
    return 1


T = int(input())
for t in range(T):
    cnt = 0
    data = []
    visited = []
    m, n, k = map(int, input().split())
    # 데이터 초기화
    for q in range(n):
        tmp = []
        for r in range(m):
            tmp.append(0)
        data.append(tmp)
    
    for j in range(k):
        x, y = map(int, input().split())
        data[y][x] = 1
        
     
    # 로직 시작
    for i in range(n):
        tmp = []
        for j in range(m):
            tmp.append(False)
        visited.append(tmp)
    
    for i in range(n):
        for j in range(m):
            if data[i][j] == 1:
                if visited[i][j] == False:
                    cnt += dfs(i,j)
    
    print(cnt)
        
