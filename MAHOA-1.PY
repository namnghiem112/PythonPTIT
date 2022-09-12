t=int(input())
while(t):
  t-=1
  s=str(input())
  i=0
  while(i<len(s)):
    count=0
    while(i<len(s)-1 and s[i]==s[i+1]): 
      count+=1
      i+=1
    print("{}{}".format(count+1,s[i]),end='')
    if(count!=0): i+=1
    else: i+=1
  print()