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
  sum=0
  for i in range(len(n)-1,-1,-1):
    if(songuyento(n[i])==0): return 0
    sum+=int(n[i])
    s+=n[i]
  if(songuyento(sum)==0 or songuyento(s)==0): return 0  
  return 1
while(t):
  t-=1
  n=int(input())
  if(n<=11):
    if(songuyento(n)==1): print("Yes")
    else: print("No")
  else:
    if(songuyento(n)==1  and kiemtra(n)==1): print("Yes")
    else: print("No")