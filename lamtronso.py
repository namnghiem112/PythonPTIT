t=int(input())
while(t):
  t-=1
  n=int(input())
  a=n
  k=0
  if(n<=10):
    print(n)
  else:
    while(a):
      s = int(n/(10**k))
      if(k>0):
        if ((s + 1) * 10**k - n <= n - s * 10**k):
          n=(s+1)*10**k
        else:
          n=s*10**k
      a=int(a/10)
      k+=1
    print(n)  