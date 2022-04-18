n = int(input())
m = int(input())
vip_seats = []              # VIP 좌석 번호
num_of_cases = [0] * (n+1)  # 각 좌석개수 별 자리 경우의 수
num_of_cases[0] = 1
num_of_cases[1] = 1
result = 0                  # 결과 값


for i in range(m):
    vip_seats.append(int(input()))
    
for i in range(2, n+1):
    num_of_cases[i] = num_of_cases[i-1] + num_of_cases[i-2]
    
for i in range(m):
    if i == 0:
        result += num_of_cases[vip_seats[0]-1]
    else:
        result *= num_of_cases[vip_seats[i] - vip_seats[i-1] - 1]
if m > 0:
    result *= num_of_cases[n - vip_seats[-1]]
else:
    result = num_of_cases[n]

print(result)