w, h = map(int, input().split())
n = int(input())

step_list = []
answer = 0

#상점과 (0,0) 사이 거리 구하기
for _ in range(n+1):
    a, b = map(int, input().split())

    if a == 1:
        step_list.append(b)
    if a == 2:
        step_list.append(2*w+h-b)
    if a == 3:
        step_list.append(2*w+2*h-b)
    if a == 4:
        step_list.append(w+b)

#동근이와 상점간의 거리 구하기
for i in range(len(step_list)-1):
    diff_value = abs(step_list[-1] - step_list[i])
    answer += min(diff_value, 2*w+2*h-diff_value)

print(answer)
