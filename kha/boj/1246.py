N, M = map(int, input().split())

input_list = []

for _ in range(M):
    input_list.append(int(input()))
input_list.sort()

#구매하고자 하는 사람이 달걀 개수보다 많으면 가장 싸게 사려는 금액부터 제거
if N < M:
    for _ in range(M-N):
        del input_list[0]
    M = N

cost = 0
skip_cnt = 0

for i in range(M):
    if input_list[i]*(M-i) > cost*(M-skip_cnt):
        cost = input_list[i]
        skip_cnt = i

print(cost, cost*(M-skip_cnt))