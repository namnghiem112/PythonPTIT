t= int(input())
while(t):
  t-=1
  s=str(input())
  if(s[0]==s[len(s)-1]): print("YES")
  else: print("NO")