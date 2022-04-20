n, m = map(int, input().split())
p_list = []
for i in range(m):
    p_list.append(int(input()))

p_list.sort()
price, cnt, result = 0, 0, 0
for i in range(m):
    cnt = m-i
    n = min(cnt, n)         # 판매 가능한 달걀, 고객수 중 작은 것
    if result < (n * p_list[i]):
        price = p_list[i]
        result = (n * p_list[i])
    
print(n,m,p_list,price, result)