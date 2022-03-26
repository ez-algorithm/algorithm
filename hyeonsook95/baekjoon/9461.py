P = [1, 1, 1, 2, 2]


def get_length(n):
    if n < len(P) + 1:
        return P[n - 1]

    while len(P) != n:
        idx = len(P) - 1
        P.append(P[idx] + P[idx - 4])
    return P[-1]


T = int(input())
for _ in range(T):
    print(get_length(int(input())))
