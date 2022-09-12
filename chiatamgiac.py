import math
t=int(input())
while(t):
  t-=1
  k,h =[float(x) for x in input().split()]
  for i in range(1,int(k)):
    print("{:.6f}".format(h*math.sqrt((float)(i)/k)),end=" ")
  print()  