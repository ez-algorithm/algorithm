# 가로 / 세로 / 대각선 중 3개가 성립되었는지 확인 
def check_Tic(check_lists):
    
    # 각 리스트의 원소 중 한개라도 3이 만들어지면, 3개가 만들어진 것을 의미 
    row = [0,0,0] 
    col = [0,0,0]
    cross = [0,0] 
    
    for check_list in check_lists:
        row[check_list[0]]+=1 # 가로 의미(열)  
        col[check_list[1]]+=1 # 세로 의미(행)
        
        # 대각선 1 체크 
        if check_list == [0,0] or check_list == [1,1] or check_list == [2,2]:
            cross[0]+=1
        
        # 대각선 2 체크 
        if check_list == [2,0] or check_list == [1,1] or check_list == [0,2]:    
            cross[1]+=1
    
    # 가로 / 세로 / 대각선 중 3개가 성립된게 1개라도 있으면 True
    if 3 in row or 3 in col or 3 in cross:
        return True
    else: 
        return False  
    
    
def solution(board):
    answer = -1
    
    # O와 X의 위치를 리스트에 좌표로 저장 
    o = []
    x = []
    
    #BORAD를 탐색하며 O과 X를 각각의 리스트에 저장 
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == 'O':
                o.append([row,col])
            elif board[row][col] == 'X':    
                x.append([row,col])
    
    # 3줄이 아예 생기지 않았을 경우 
    if check_Tic(o) == False and check_Tic(x) == False:
        # 가능 CASE 1) 선공 후공이 같은 횟수로 진행된 경우
        # 가능 CASE 2) 선공이 한번 더 진행된 경우 
        if len(o) == len(x) or len(o) == len(x)+1: 
            answer = 1
        else:
            answer = 0
    elif check_Tic(o): # O가 3개 만들어졌을 경우 
        # 선공이 먼저 3개가 만들어진 경우 -> O 개수가 X보다 1개 더 많다 
        # 이때 X는 3개가 성립된게 없어야 함 
        if len(o) == len(x) + 1 and check_Tic(x) == False:
            answer = 1
        else: 
            answer = 0
    elif check_Tic(x): # X만 3개 성립된 경우 
        # 후공이 놓고 3개가 성립되어야 하니, O과 X의 개수가 동일 
        # 이때 O은 3개가 성립된게 없어야 함 
        if len(o) == len(x) and check_Tic(o) == False:
            answer = 1
        else:
            answer = 0
    else: 
        answer = 0    
        
    return answer