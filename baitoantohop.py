n,k=[int(x) for x in input().split()]
se = set()
se = {int(x) for x in input().split()}
lis = list(se)
lis.sort()
n=len(lis)
a=[0]
ok=1
def khoitao():
  global a
  global k
  for i in range(1,k+1):
    a.append(i)
def sinh():
  global a
  global k
  global ok
  i=k
  while(i>=1 and a[i]==n-k+i): i-=1
  if(i==0): ok=0
  else: a[i]+=1
  p=a[i]
  while(i<=k):
    i+=1
    p+=1
    if(i<=k): a[i]=p
khoitao()
ok=1
while(ok):
  for i in range(1,k+1):
    print(lis[a[i]-1],end=' ')
  print()
  sinh()
  