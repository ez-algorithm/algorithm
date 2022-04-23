import sys

input = sys.stdin.readline

N, M = map(int, input().split())
P = sorted([int(input()) for _ in range(M)], reverse=True)

price = P[-1]
amount = -1

for idx, p in enumerate(P[: N - 1]):
    if amount < (idx + 1) * p:
        price = p
        amount = (idx + 1) * p
print(p, amount)
