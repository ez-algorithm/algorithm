from collections import Counter


def solution(R, C, K):
    maps = [list(map(int, input().strip().split())) for _ in range(3)]

    def transpose(lst):
        return list(map(list, zip(*lst)))

    def calculate(lst):
        new = []
        max_size = 0
        for row in lst:
            size = 0
            column = []
            for val in sorted(Counter(row).items(), key=lambda x: (x[1], x[0])):
                if val[0] > 0:
                    size += 2
                    column.extend(list(val))
                if size > 100:
                    break
            new.append(column)
            max_size = max(max_size, size)

        for r in range(len(new)):
            for _ in range(len(new[r]), max_size):
                new[r].append(0)
        return new

    T = 0
    r, c = 3, 3
    while T <= 100:
        if -1 < R - 1 < r and -1 < C - 1 < c and maps[R - 1][C - 1] == K:
            return T
        T += 1

        if r >= c:
            maps = calculate(maps)
        else:
            maps = transpose(calculate(transpose(maps)))
        r, c = len(maps), len(maps[0])

    return -1


if __name__ == "__main__":
    R, C, K = map(int, input().split())
    print(solution(R, C, K))
