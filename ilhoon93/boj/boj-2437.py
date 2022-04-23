n = int(input())
weights = list(map(int,input().split()))
w = 1

weights.sort()
for x in weights:
    if x > w:
        break
    else:
        w=w+x
print(w)
