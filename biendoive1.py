def printCollatz(n):
    count=0
    while n != 1:
        count+=1
        if n%2==1:
            n = 3 * n + 1
        else:
            n = n // 2
    print(count+1)
while(1):
  n=int(input())
  if(n==0): break
  printCollatz(n) 