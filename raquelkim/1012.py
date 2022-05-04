from collections import deque
t = int(input())

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs(field, a, b):
    queue = deque()
    queue.append((a,b))
    field[a][b] = 0

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0 <= nx < n and 0 <= ny < m and field[nx][ny] == 1:
                field[nx][ny] = 0
                queue.append((nx, ny))
    return

for i in range(t):
    m, n, k = map(int,input().split())
    field = [[0] * m for i in range(n)]
    cnt = 0

    for j in range(k):
        x, y = map(int,input().split())
        field[y][x] = 1
    
    for a in range(n):
        for b in range(m):
            if field[a][b] == 1:
                bfs(field, a, b)
                cnt += 1
    print(cnt)

    

