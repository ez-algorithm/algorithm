import sys

input = sys.stdin.readline

N = int(input().strip())
nums = list(map(int, input().strip().split(" ")))
sums = [0] * len(nums)

sums[0] = nums[0]
for idx in range(1, len(nums)):
    sums[idx] = sums[idx - 1] + nums[idx]

T = int(input().strip())
for _ in range(T):
    start, end = map(int, input().strip().split(" "))

    if start == 0:
        print(sums[end])
    else:
        print(sums[end] - sums[start - 1])
