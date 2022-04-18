import sys

input = sys.stdin.readline

N = int(input())
tops = list(map(int, input().split()))
tops = [(i + 1, t) for i, t in enumerate(tops)]

answer = []
stack = []

for idx, top in tops:
    while stack and stack[-1][1] <= top:
        stack.pop()
    answer.append(stack[-1][0] if stack else 0)
    stack.append((idx, top))

print(*answer)
