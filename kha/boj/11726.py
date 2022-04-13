n = int(input())
dptable = [0]*(n+1)

def DP(n):
  if n == 0:
    return 1
  if n < 0:
    return 0
  if dptable[n] > 0:
    return dptable[n]
  
  dptable[n] = DP(n-1) + DP(n-2)
  return dptable[n]

print(DP(n)%10007)


