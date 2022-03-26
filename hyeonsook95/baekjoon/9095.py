import sys

input = sys.stdin.readline


def solution(N):
    def dfs(number, count):
        if number == 0:
            return count + 1

        for num in [1, 2, 3]:
            if number - num >= 0:
                count = dfs(number - num, count)
        return count

    return dfs(N, 0)


if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        print(solution(int(input())))
