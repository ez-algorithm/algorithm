n,m = map(int, input().split())
array = [0] * m
for i in range(m):
    array[i] = int(input())
array.sort()

result = 0  #수익 
target = 0 #달걀 책정금액
for i in range(m):
    egg = min(m-i, n)  #달걀갯수보다 사람 수가 더 많으면 달걀 갯수까지만 팔게 하기.

    if result < array[i] * egg:
        result = array[i] * egg
        target = array[i]

print(target, array)

