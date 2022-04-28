N = int(input())
input_list = list(map(int, input().split()))

answer_list = []

answer_list.append(0)


for i in range(1, N):
    pivot = input_list[i]
    
    if pivot <= input_list[i-1]:
        answer_list.append(i)
        continue

    idx = answer_list[i-1]

    for k in range(idx-1, -1, -1):
        if pivot <= input_list[k]:
            answer_list.append(k+1)
            break
    else:
        answer_list.append(0)
    
print(' '.join(list(map(str, answer_list))))
