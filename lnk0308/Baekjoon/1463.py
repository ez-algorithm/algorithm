# def solution(n):
#     list =[]

#     list.append([n,0])
    
#     while(len(list) > 0):
#         check_num, cnt = list.pop(0)

#         if check_num == 1:
#             return cnt
        
#         if check_num % 3 == 0:
#             list.append([check_num/3,cnt+1])
        
#         if check_num % 2 == 0:
#             list.append([check_num/2,cnt+1])
        
#         list.append([check_num-1,cnt+1])
                       

# n = int(input())
# print(solution(n))


# def Solution (n):
    
#     if n == 1:
#        return 0
#     elif memo[n] > 0:
#         return memo[n]
    
#     cnt = Solution(n-1)  
    
    # if n % 3 == 0:
    #     cnt = min(cnt, Solution(n//3))
        
    # if n % 2 == 0:
    #     cnt = min(cnt, Solution(n//2))
            
#     cnt+=1
    
#     memo[n] = cnt
#     return memo[n]    

# n = int(input())
# memo = [0] * (n+1)
# print(Solution(n))



n = int(input())
memo = [0] * (n+1)

for i in range(2,n+1):
    memo[i] = memo[i-1] 
    
    if i % 2 == 0:
        memo[i] = min(memo[i], memo[i//2])
        
    if i % 3 == 0:
        memo[i] = min(memo[i], memo[i//3])
        
    memo[i]+= 1 
    
print(memo[n])
        

