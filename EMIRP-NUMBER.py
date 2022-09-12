t= int(input())
import math
def songuyento(n):
  n=int(n)
  if(n<2): return 0
  for i in range(2,int(math.sqrt(n))+1):
    if(n%i==0): return 0
  return 1
def kiemtra(n):
  n=str(n)
  s=""
  for i in range(len(n)-1,-1,-1):
    s+=n[i]
  return s
while(t):
  t-=1
  n=int(input())
  for i in range(13,n+1,2):
    k = int(kiemtra(i))
    if(k<n and i!=k and i<k):
      if(songuyento(i)==1 and songuyento(k)==1):
        print("{} {}".format(i,k),end=' ')
  print()