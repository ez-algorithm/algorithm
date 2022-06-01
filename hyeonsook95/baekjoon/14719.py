import sys

input = sys.stdin.readline
H, W = map(int, input().strip().split())
heights = list(map(int, input().strip().split()))

water = 0
stack = []
pivot = heights[0]

for idx in range(1, W):
    current_height = heights[idx]
    if current_height > pivot or idx == W - 1:
        min_pivot = min(pivot, current_height)
        while stack:
            prev_height = stack.pop()
            if min_pivot - prev_height > 0:
                water += min_pivot - prev_height
            else:
                min_pivot = prev_height
        pivot = current_height
    else:
        stack.append(current_height)
print(water)
