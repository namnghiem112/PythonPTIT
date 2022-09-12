t= int(input())
res = [1,1,2,6,24,120,720,5040,40320,362880]
def kt(n):
  n=str(n)
  sum=0
  for i in range(0,len(n)):
    sum += res[int(n[i])]
  if(sum==int(n)): return 1
  else:
    return 0
while(t):
  t-=1
  n=int(input())
  if(kt(n)==1): print("Yes")
  else: print("No")