t = int(input())
while(t):
  t-=1
  n = int(input())
  s = str(input())
  res =""
  list=[]
  k=0
  if(n==2): print(s)
  elif(n==8): k=3
  elif(n==16): k=4
  elif(n==4): k=2
  if(k!=0):
    while(len(s)%k!=0): s="0"+s
    for i in range(len(s)-1,-1,-1):
      res+=s[i]
    i=0
    while(i<len(res)):
      tmp=""
      tmp=res[i:i+k]
      sum=0
      for j in range(0,k):
        if(tmp[j]=="1"):
          sum+=2**j
      if(sum<=9):list.append(sum)    
      elif(sum==10):list.append("A")
      elif(sum==11):list.append("B")
      elif(sum==12):list.append("C")
      elif(sum==13):list.append("D")
      elif(sum==14):list.append("E")
      elif(sum==15):list.append("F")      
      i+=k
    list.reverse()  
    for x in list:
      print(x,end='')
    print(end='\n')
    
    
  