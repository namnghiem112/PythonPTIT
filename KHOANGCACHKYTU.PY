t=int(input())
while(t):
  t-=1
  s=str(input())
  s2=""
  for i in range(len(s)):
    s2=str(s[i])+s2
  check=0
  for i in range(1,len(s)):
    if(abs(ord(s[i])-ord(s[i-1]))!=abs(ord(s2[i])-ord(s2[i-1]))):
      check=1
  if(check==0): print("YES")
  else: print("NO")