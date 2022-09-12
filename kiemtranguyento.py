import math
def kiemtra(n):
  if(n<2): return False
  for i in range(2,int(math.sqrt(n))+1):
    if(n%i==0): return False
  return True    
n,m = [int(x) for x in input().split()]
a=[]
for i in range(n):
  a.append(list(map(int,input().split())))
for i in range(n):
  for j in range(m):
    if(kiemtra(a[i][j])==True): a[i][j]=1
    else: a[i][j]=0
for i in range(n):
  print(*a[i])
  