t=int(input())
while(t):
  t-=1
  n=int(input())
  a=[int(x) for x in input().split()]
  b=[1]*(n+5)
  list=[]
  for i in range(n):
    if len(list)!=0: top=list[len(list)-1]
    while(len(list)!=0 and a[i]>=a[top]):
      b[i]+=b[top]
      list.pop()
      if len(list)!=0: top=list[len(list)-1]
    list.append(i)
    # print(i,b[i])
  for i in range(n):
    print(b[i],end=" ")
  print()  