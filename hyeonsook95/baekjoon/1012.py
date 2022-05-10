import sys
from collections import deque

input = sys.stdin.readline

# 이동 방향
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

T = int(input().strip())
for _ in range(T):
    M, N, K = map(int, input().split())
    visited = [[False for _ in range(M)] for _ in range(N)]

    # 배추 위치 입력
    maps = [[False for _ in range(M)] for _ in range(N)]
    for _ in range(K):
        c, r = map(int, input().split())
        maps[r][c] = True

    def bfs(start_v):
        q = deque([start_v])
        visited[start_v[0]][start_v[1]] = True

        while q:
            v = q.popleft()
            for d in range(4):
                if (
                    -1 < v[0] + dr[d] < N
                    and -1 < v[1] + dc[d] < M
                    and maps[v[0] + dr[d]][v[1] + dc[d]]
                    and not visited[v[0] + dr[d]][v[1] + dc[d]]
                ):
                    q.append((v[0] + dr[d], v[1] + dc[d]))
                    visited[v[0] + dr[d]][v[1] + dc[d]] = True

    count = 0
    for r in range(N):
        for c in range(M):
            if not visited[r][c] and maps[r][c]:
                count += 1
                bfs((r, c))
            else:
                visited[r][c] = True

    print(count)
