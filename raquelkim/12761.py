from collections import deque

def bfs():
    visit = [0 for i in range(100001)]
    visit[n] = 1 
    d = [1, -1, a, -a, b, -b, a, b]
    queue = deque()
    queue.append(n)

    while queue:
        x = queue.popleft()
        for i in range(8):
            if i < 6:
                nx = x + d[i]
                if 0 <= nx <= 100000 and visit[nx] == 0:
                    queue.append(nx)
                    visit[nx] = 1
                    s[nx] = s[x] + 1
            else:
                nx = x * d[i]
                if 0 <= nx <= 100000 and visit[nx] == 0:
                    queue.append(nx)
                    visit[nx] = 1
                    s[nx] = s[x] + 1

a, b, n, m = map(int, input().split())
s = [0 for i in range(100001)]
bfs()
print(s[m])
