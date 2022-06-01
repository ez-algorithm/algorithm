h, w = map(int, input().split())

height_list = list(map(int, input().split()))

criteria_idx = 0
answer = 0
temp = 0

for i in range(w):
    #기준보다 현재 높이가 더 높다면 기준을 변경
    if height_list[criteria_idx] <= height_list[i]:
        criteria_idx = i
        temp = 0
        continue
    answer += height_list[criteria_idx]-height_list[i]
    temp += height_list[criteria_idx]-height_list[i]

last_criteria_idx = criteria_idx
criteria_idx = w-1
#마지막 기준 ~ 가장 끝의 오프셋까지는 역순으로 다시 계산
for i in range(w-1, last_criteria_idx-1, -1):
    #기준보다 현재 높이가 더 높다면 기준을 변경
    if height_list[criteria_idx] <= height_list[i]:
        criteria_idx = i
        continue
    answer += height_list[criteria_idx]-height_list[i]

print(answer-temp)
    