from collections import deque

puyo_field = []

for _ in range(12):
    puyo_field.append(list(input()))

#뿌요의 삭제를 쉽게 하기 위해 전치행렬로 변환
puyo_field = list(map(list, zip(*puyo_field)))


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def BFS(x, y, target):
    myq = deque([])
    pos_list = [] #같은 타입의 뿌요들의 좌표 리스트
    myq.append([x, y])

    while myq:

        cur = myq.pop()

        #상하좌우에 같은 뿌요가 있는지 탐색
        for idx in range(4):
            cur_x = cur[0] + dx[idx]
            cur_y = cur[1] + dy[idx]
            if cur_x < 6 and cur_x >= 0 and cur_y < 12 and cur_y >= 0 and puyo_field[cur_x][cur_y] == target and puyo_field[cur_x][cur_y] != 'x':
                myq.append([cur_x, cur_y])
                pos_list.append([cur_x, cur_y])
                puyo_field[cur_x][cur_y] = 'x'
    
    #만약 터트릴 수 있는 뿌요 개수가 4개 미만이면 x로 바꾼 뿌요들을 다시 원복해야 함
    if len(pos_list) < 4:
        for i in range(len(pos_list)):
            puyo_field[pos_list[i][0]][pos_list[i][1]] = target


combo_cnt = 0 #연쇄 발생 횟수

while (True):
  isFinish = True
  for i in range(6):
    for k in range(12):
        #빈 공간이거나 이미 터트려야 할 뿌요가 아닌 경우 탐색
        if puyo_field[i][k] != '.' and puyo_field[i][k] != 'x':
            BFS(i, k, puyo_field[i][k])

  for i in range(6):
    for k in range(12):
        #터트릴 뿌요라면 해당 뿌요를 삭제
        if puyo_field[i][k] == 'x': 
            isFinish = False
            puyo_field[i].pop(k)
            puyo_field[i].insert(0, '.')

  if isFinish:
    print(combo_cnt)
    break

  combo_cnt += 1