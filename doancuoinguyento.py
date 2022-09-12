t=int(input())
import math
def songuyento(n):
  n=int(n)
  if(n<2): return 0
  for i in range(2,int(math.sqrt(n))+1):
    if(n%i==0): return 0
  return 1
while(t):
  t-=1
  s=str(input())
  res = s[-4:]
  if(songuyento(res)==1): print("YES")
  else: print("NO")