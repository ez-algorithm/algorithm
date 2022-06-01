from collections import deque
a, b, n, m = map(int, input().split())
visit_list = [0]*100001
myq = deque([])

#처음 시작은 (동규 시작위치, 이동횟수 0회)
myq.append([n, 0])

while myq:
    cur = myq.popleft()

    if cur[0] == m:
        print(cur[1])
        break

    #이동 가능한 케이스를 모두 탐색
    if cur[0]+1 <= 100000 and visit_list[cur[0]+1]==0:
        myq.append([cur[0]+1, cur[1]+1])
        visit_list[cur[0]+1]=1
    if cur[0]-1 >= 0 and visit_list[cur[0]-1]==0:
        myq.append([cur[0]-1, cur[1]+1])
        visit_list[cur[0]-1]=1
    if cur[0]+a <= 100000 and visit_list[cur[0]+a]==0:
        myq.append([cur[0]+a, cur[1]+1])
        visit_list[cur[0]+a]=1
    if cur[0]-a >= 0 and visit_list[cur[0]-a]==0:
        myq.append([cur[0]-a, cur[1]+1])
        visit_list[cur[0]-a]=1
    if cur[0]+b <= 100000 and visit_list[cur[0]+b]==0:
        myq.append([cur[0]+b, cur[1]+1])
        visit_list[cur[0]+b]=1
    if cur[0]-b >= 0 and visit_list[cur[0]-b]==0:
        myq.append([cur[0]-b, cur[1]+1])
        visit_list[cur[0]-b]=1
    if cur[0]*a <= 100000 and visit_list[cur[0]*a]==0:
        myq.append([cur[0]*a, cur[1]+1])
        visit_list[cur[0]*a]=1
    if cur[0]*b <= 100000 and visit_list[cur[0]*b]==0:
        myq.append([cur[0]*b, cur[1]+1])
        visit_list[cur[0]*b]=1

