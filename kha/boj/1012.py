import collections
  
def BFS(start_x, start_y):
  dx = [0, 0, -1, 1]
  dy = [-1, 1, 0, 0]

  myq = collections.deque()
  myq.append((start_x, start_y))

  while myq:
    cur_x, cur_y = myq.popleft()

    #현재 양배추 기준으로 상하좌우 탐색
    for i in range(4):

      next_x = cur_x + dx[i]
      next_y = cur_y + dy[i]

      if next_x >= 0 and next_x < m and next_y >= 0 and next_y < n:
        #주변에 양배추가 있다면
        if table[next_x][next_y] == 1:
          myq.append((next_x, next_y))
          table[next_x][next_y] = 0 #이미 탐색한 양배추 자리는 0으로 표기
          
t = int(input())

for _ in range(t):
  m, n, k = map(int, input().split())
  table = [[0]*n for _ in range(m)]
  
  for _ in range(k):
    a, b = map(int, input().split())
    table[a][b] = 1 #양배추가 있는 자리는 1로 표시

  result = 0

  for i in range(m):
    for j in range(n):
      #해당 자리에 양배추가 있다면
      if table[i][j] == 1:
        BFS(i, j)
        result += 1

  print(result)
