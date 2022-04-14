import sys
from collections import defaultdict, deque

MAX = 1000000001
input = sys.stdin.readline

N, Q = map(int, input().split())

graph = defaultdict(list)
weights = [[MAX for _ in range(N + 1)] for _ in range(N + 1)]

for _ in range(N - 1):
    p, q, r = map(int, input().split())

    graph[p].append(q)
    graph[q].append(p)

    # 가중치 입력
    weights[p][q] = r
    weights[q][p] = r

# bfs
def bfs(start_v):
    visited = [False for _ in range(N + 1)]
    visited[start_v] = True
    usado = [MAX for _ in range(N + 1)]
    queue = deque([start_v])

    while queue:
        v = queue.popleft()
        for w in graph[v]:
            if not visited[w]:
                usado[w] = min([usado[w], usado[v], weights[v][w]])

                visited[w] = True
                queue.append(w)
    return usado


# v 영상과 k 이상의 유사도를 가진 영상의 개수
for _ in range(Q):
    k, v = map(int, input().split())
    usado = bfs(v)
    print(len([w for w in usado if k <= w]) - 2)
