t= int(input())
import math
def songuyento(n):
  if(n<2): return 0
  for i in range(2,int(math.sqrt(n))+1):
    if(n%i==0): return 0
  return 1    
while(t):
  t-=1
  n=int(input())
  count =0
  for i in range(5,n+1,2):
    if(songuyento(i)==1 and songuyento(i+6)==1 and i+6<n):
      if(songuyento(i+2)==1 or songuyento(i+4)==1):
        count+=1
  print(count)    