t=int(input())
import math
ok=0
while t:
    t-=1
    n=int(input())
    x=math.ceil(pow(n,1.0/3))
    if(x**3==n): print("YES")
    else: print("NO")
    