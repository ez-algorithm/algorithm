import sys

input = sys.stdin.readline

maps = [0] * 1000001

N, K = map(int, input().strip().split(" "))

for _ in range(N):
    ice, idx = map(int, input().strip().split(" "))
    maps[idx] = ice

result = sum(maps[: 2 * K])
p_sum = result
left, right = 0, 2 * K
while right < 1000000:
    left += 1
    right += 1

    p_sum = p_sum - maps[left - 1] + maps[right]
    result = max(result, p_sum)


print(result)
