def solution(n):
    answer = []
    value_list = [[0]*n for _ in range(n)]
    
    row = -1
    col = 0
    val = 1
    
    for i in range(n):
        if i%3 == 0:
            #방향이 아래로 가는 경우
            for k in range(n-i):
                row += 1
                value_list[row][col] = val
                val += 1
        elif i%3 == 1:
            #방향이 오른쪽으로 가는 경우
            for k in range(n-i):
                col += 1
                value_list[row][col] = val
                val += 1
        elif i%3 == 2:
            #방향이 대각선 위로 가는 경우
            for k in range(n-i):
                col -= 1
                row -= 1
                value_list[row][col] = val
                val += 1
        
    for i in range(n):
        for k in range(n):
            if value_list[i][k] != 0:
                answer.append(value_list[i][k])
            
    
    return answer
