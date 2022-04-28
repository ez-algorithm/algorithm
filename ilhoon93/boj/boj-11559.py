import copy
import pprint
global rows 
rows = 12
global cols
cols = 6
global seq
seq = 0

def puyo(data, checked):
    global rows, cols, seq
    result = False
    for i in range(rows):
        for j in range(cols):
            if checked[i][j]==False and data[i][j] != '.':
                dfs(i, j, data[i][j], data, checked)
                if seq>=4:
                    result = True
                    bomb(i, j, data[i][j], data, checked)
                seq = 0
    return result
                
def bomb(i, j, c, data, checked):
    data[i][j] = '.'
    
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]
    
    for x in range(4):
        ni = i + di[x]
        nj = j + dj[x]
        
        if ni < 0 or nj < 0 or ni >= rows or nj >= cols:
            continue
        if data[ni][nj] == c and checked[ni][nj] == True:
            bomb(ni, nj, c, data, checked)

def dfs(i, j, c, data, checked):
    
    global rows, cols, seq
    seq += 1
    checked[i][j] = True
    
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]
    
    for x in range(4):
        ni = i + di[x]
        nj = j + dj[x]
        
        if ni < 0 or nj < 0 or ni >= rows or nj >= cols:
            continue
        if data[ni][nj] == c and checked[ni][nj] == False:
            dfs(ni, nj, c, data, checked)
# 메인
cnt = 0
dataOrg = []
checked = []
for i in range(rows):
    dataOrg.append(list(map(str, input())))
    checked.append(list([False]*cols))
    
data = copy.deepcopy(dataOrg)
while True:
    for i in range(rows):
        for j in range(cols):
            checked[i][j] = False
    
    if puyo(data, checked):
        cnt += 1
        
        # 아래로 땡기기
        for j in range(cols):
            for i in range(rows-1, -1, -1):
                if data[i][j] == '.':
                    for r in range(i, -1, -1):
                        if data[r][j] != '.':
                            tmp = data[i][j]
                            data[i][j] = data[r][j]
                            data[r][j] = tmp
                            break
    else:
        break
print(cnt)
