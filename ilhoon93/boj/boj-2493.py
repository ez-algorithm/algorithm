n = int(input())
t_list = list(map(int,input().split()))

tops = [(t_list[0],1)]
result = [0]

for i in range(1, n):
    tmp = 0
    while tops:
        if t_list[i] >= tops[-1][0]:
            tops.pop()
        else:
            tmp = tops[-1][1]
            break

    result.append(tmp)
    
    tops.append((t_list[i], i+1))
print(" ".join(map(str, result))
