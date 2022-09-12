t=int(input())
def kiemtra(n):
  if(n<22 or n%2==1): return 0
  count=0
  sum=0
  res=n
  while(n!=0):
    p=n%10
    if(p%2==1): return 0
    sum=sum*10+p
    count+=1
    n=int(n/10)
  if(count%2==1 or sum!=res):return 0
  return 1
while(t):
  t-=1
  n=int(input())
  for i in range(22,n,2):
    if(kiemtra(i)==1): print(i,end=" ")
  print()    
      
  