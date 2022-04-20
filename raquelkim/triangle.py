# answer = 삼각형 배열
# x, y = 좌표값
# num = 대입숫자
# i = 방향값
# j = i 방향에 대한 대입 횟수
def solution(n):
    answer = [[0 for j in range(1, i+1)] for i in range(1, n+1)]
    x, y = -1, 0
    num = 1
    for i in range(n):
        for j in range(i, n):
            if i % 3 == 0: # 하
                x += 1
            elif i % 3 == 1: # 우
                y += 1
            else:  # 상
                x -= 1
                y -= 1
            answer[x][y] = num
            num += 1
        return sum(answer, [])  # 이차열 리스트를 일차열 리스틀

