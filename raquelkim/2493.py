import sys
n = int(sys.stdin.readline())
arr = list(map(int,input().split()))

stack = []   #인덱스와 탑의 높이 
stack.append([1, arr[0]])
result = [0] 

for i in range(1, n):
    while stack:
        if stack[-1][1] >= arr[i]:
            result.append(stack[-1][0])
            stack.append([i + 1, arr[i]])
            break
        else:
            stack.pop()
    if not stack:
        result.append(0)
        stack.append([i + 1, arr[i]])

print(*result, end='')


