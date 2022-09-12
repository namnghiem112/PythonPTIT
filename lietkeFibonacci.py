f=[0]*93
def snt():
  global f
  f[1]=1
  f[2]=1
  for i in range(3,93):
    f[i]=f[i-1]+f[i-2]
snt()
t=int(input())
while(t):
  t-=1
  a,b = [int(x) for x in input().split()]
  for i in range(a,b+1):
    print(f[i],end=' ')
  print()  