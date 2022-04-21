N = int(input())
mylist = list(map(int, input().split()))
mylist.sort()

max_value = 0
result = sum(mylist)+1 #default는 전체 추를 다 올린 값+1

for i in range(N):
  if mylist[i] > max_value + 1:
    result = max_value + 1
    break
  else:
    max_value += mylist[i]

print(result)