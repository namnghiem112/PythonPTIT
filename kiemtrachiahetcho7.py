def dao(n):
  sum=0
  while(n!=0):
    p=n%10
    sum=sum*10+p
    n//=10
  return sum  
t=int(input())
while(t):
  t-=1
  i=1;
  n=int(input())
  check=0
  while(i<=1000):
    i+=1
    if(n%7==0):
      print(n)
      check=1
      break
    else:
      if(dao(n)+n %7==0):
        print(n+dao(n))
        check=1
        break
      else:
        n=n+dao(n)   
  if(check==0): print("-1")      
      