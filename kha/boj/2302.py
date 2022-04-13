N = int(input())
M = int(input())
dptable = [0]*41

def DP(n):
  if n == 1:
    return 1
  if n == 2:
    return 2
  if dptable[n] != 0:
    return dptable[n]

  dptable[n] = DP(n-1) + DP(n-2)
  return dptable[n]

fix_seat_list = []

fix_seat_list.append(0)

for _ in range(M):
  fix_seat_list.append(int(input()))

fix_seat_list.append(N+1)

#VIP석을 기준으로 분리된 자리 수
separated_size_list = []

for i in range(M+1):
  separated_size_list.append(fix_seat_list[i+1]-fix_seat_list[i]-1)

answer = 1

#분리된 자리의 교환 경우의 수끼리 곱함
for i in range(len(separated_size_list)):
  if separated_size_list[i] == 0:
    continue
  answer *= DP(separated_size_list[i])

print(answer)
