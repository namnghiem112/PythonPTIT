t=int(input())
while(t):
  t-=1
  n,k=[int(x) for x in input().split()]
  len = 2**(n-1)
  while True:
    if(n==1):
      print("A")
      break
    if(len==k):
      print(chr(n+64))
      break
    if(k>len):
      k=len-(k-len)
    n-=1
    len//=2