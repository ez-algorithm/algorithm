import sys

input = sys.stdin.readline
dp = [1, 1, 2, 3]  # dp 초기화

N = int(input())
# N은 최대 40까지이므로 dp의 최대 길이도 40, O(N) = 40
while N > len(dp) - 1:
    dp.append(dp[-1] + dp[-2])

M = [int(input()) for _ in range(int(input()))]

if not M:
    print(dp[N])
else:
    M.append(N + 1)
    answer = dp[M[0] - 1]
    for idx in range(1, len(M)):
        answer *= dp[M[idx] - M[idx - 1] - 1]
    print(answer)
