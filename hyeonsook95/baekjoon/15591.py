import sys

MAX = 1000000001
input = sys.stdin.readline


N, Q = map(int, input().split())

path = [[False for _ in range(N + 1)] for _ in range(N + 1)]
weights = [[MAX for _ in range(N + 1)] for _ in range(N + 1)]

for _ in range(N - 1):
    p, q, r = map(int, input().split())

    path[p][q] = True
    path[q][p] = True

    # 가중치 입력
    weights[p][q] = r
    weights[q][p] = r

# 플로이드 와샬
for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if i == j:
                continue
            if path[i][k] and path[k][j]:
                weights[i][j] = min([weights[i][j], weights[i][k], weights[k][j]])

# v 영상과 k 이상의 유사도를 가진 영상의 개수
for _ in range(Q):
    k, v = map(int, input().split())
    print(len([w for w in weights[v] if k <= w]) - 2)
