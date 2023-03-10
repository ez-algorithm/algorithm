def solution(board):
    b = { 'O': 1, '.': 0, 'X': -1 }
    
    board = [ [ b[board[r][c]] for c in range(3) ] for r in range(3) ]
    rotated = list(zip(*board))
    sum_board = sum(sum(board, []))

    fw, sw = 0, 0
    for r in range(3):
        os = sum(board[r])
        rs = sum(rotated[r])
        if os == 3 or rs == 3:
            fw += 1
        if os == -3 or rs == -3:
            sw += 1
    
    fc = sum([board[0][0], board[1][1], board[2][2]])
    sc = sum([board[0][2], board[1][1], board[2][0]])
    if fc == 3 or sc == 3:
        fw += 1
    if fc == -3 or sc == -3:
        sw += 1


    if fw > 2 or sw > 2 or (fw > 0 and sw > 0):
        return 0
    if sum_board < 0 or sum_board > 1:
        return 0
    if (fw > 0 and sum_board == 0) or (sw > 0 and sum_board == 1):
        return 0
    return 1