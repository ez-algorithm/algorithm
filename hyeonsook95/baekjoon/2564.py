import sys

input = sys.stdin.readline
C, R = map(int, input().strip().split())

stores = []
for _ in range(int(input().strip()) + 1):
    direction, distance = map(int, input().strip().split())

    # 1 북쪽, 2 남쪽, 3 서쪽, 4 동쪽
    # 1 or 2는 왼쪽 경계로부터의 거리
    # 3 or 4는 위쪽 경계로부터의 거리
    if direction == 1:
        stores.append((R, distance))
    elif direction == 2:
        stores.append((0, distance))
    elif direction == 3:
        stores.append((R - distance, 0))
    elif direction == 4:
        stores.append((R - distance, C))

# 동근이의 위치
start_r, start_c = stores.pop()

# 방향 좌표
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def dfs(end_r, end_c):
    visited = [[False for _ in range(C + 1)] for _ in range(R + 1)]
    visited[start_r][start_c] = True
    stack = [(start_r, start_c, 0)]
    min_distance = (R + C + 1) * 2

    while stack:
        vr, vc, vd = stack.pop()
        for d in range(4):
            # R 좌표, C 좌표, 해당 좌표까지의 거리
            wr, wc, wd = vr + dr[d], vc + dc[d], vd + 1

            # 상점에 도착하면 최소 거리값을 계산
            if (wr, wc) == (end_r, end_c):
                min_distance = min(min_distance, wd)
                continue

            if (
                -1 < wr < R + 1
                and -1 < wc < C + 1
                and not visited[wr][wc]
                and (wr == 0 or wr == R or wc == 0 or wc == C)
            ):

                stack.append((wr, wc, wd))
                visited[wr][wc] = True

    return min_distance


sum = 0
for store_r, store_c in stores:
    sum += dfs(store_r, store_c)

print(sum)
