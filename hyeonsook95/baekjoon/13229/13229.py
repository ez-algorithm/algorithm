import sys

input = sys.stdin.readline

N = int(input().strip())
nums = list(map(int, input().strip().split(" ")))

T = int(input().strip())
for _ in range(T):
    start, end = map(int, input().strip().split(" "))
    print(sum(nums[start : end + 1]))
