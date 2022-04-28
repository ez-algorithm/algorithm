import sys

input = sys.stdin.readline
dp = [0, 1, 2]

N = int(input())
while N > len(dp) - 1:
    dp.append((dp[-1] + dp[-2]) % 10007)
print(dp[N])
