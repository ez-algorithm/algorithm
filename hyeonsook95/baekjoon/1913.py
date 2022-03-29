import sys

input = sys.stdin.readline

N = int(input().strip())
maps = [[0 for _ in range(N)] for _ in range(N)]

dr, dc = [1, 0, -1, 0], [0, 1, 0, -1]

d_idx = 0
r_idx, c_idx = 0, 0
for num in range(N**2, 0, -1):
    maps[r_idx][c_idx] = num
    if not (
        -1 < r_idx + dr[d_idx] < N
        and -1 < c_idx + dc[d_idx] < N
        and maps[r_idx + dr[d_idx]][c_idx + dc[d_idx]] == 0
    ):
        d_idx = (d_idx + 1) % 4
    r_idx += dr[d_idx]
    c_idx += dc[d_idx]

for m in maps:
    print(*m, sep=" ", end="\n")
