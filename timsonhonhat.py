t= int(input())
while(t!=0):
  t-=1
  s=str(input())
  list = []
  i=0
  n=len(s)
  while(i<n):
    index = i
    res = ""
    test=0
    while(i<n and s[i].isdigit()==True): 
      i+=1
      test=1
    if(test==1):
      res = s[index:i]
    else:
      i+=1
    if(res != ""): list.append(int(res))
  print(min(list))  
  