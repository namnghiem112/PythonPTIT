a=[0]*4
def kiemtra():
  dem=0
  global a
  for i in range(1,4):
    if(a[i]==a[0]): dem+=1
  if(dem==3): return 0
  return 1  
def biendoi():
  global a
  count =0
  while(kiemtra()):
    count+=1
    x=a[0]
    for i in range(0,3):
      a[i]=abs(a[i]-a[i+1])
    a[3]=abs(a[3]-x)
  print(count)  
while(1):
  a=[int(x) for x in input().split()]  
  if(a[0]==0 and a[1]==0 and a[2]==0 and a[3]==0): break
  biendoi()