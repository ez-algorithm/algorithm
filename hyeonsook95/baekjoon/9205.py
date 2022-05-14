import sys

input = sys.stdin.readline
MAX_BEER_CNT = 20


def solution():
    N = int(input().strip())
    postions = [(map(int, input().strip().split())) for _ in range(N + 2)]

    dist = 0
    pre_x, pre_y = postions[0]

    for cur_x, cur_y in postions[1:]:
        dist += abs(pre_x - cur_x) + abs(pre_y - cur_y)

        drunk, dist = divmod(dist, 50)
        pre_x, pre_y = cur_x, cur_y
        if MAX_BEER_CNT - drunk < 0:
            return "sad"

    return "happy"


T = int(input().strip())
for _ in range(T):
    print(solution())
