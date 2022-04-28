r = 31
M = 1234567891

N = int(input())
S = list(map(lambda char: ord(char) - 96, input()))
for idx in range(N):
    S[idx] = S[idx] * (r**idx)
print(sum(S))
print(sum(S) % M)
