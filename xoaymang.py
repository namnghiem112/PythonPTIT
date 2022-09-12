t = int(input())
while(t):
  t-=1
  n,k = [int(i) for i in  input().split()]
  list = [int(x) for x in input().split()]
  print(*list[k:n],end=" ")
  print(*list[0:k])