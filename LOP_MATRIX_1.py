def chuyenvi(a,hang,cot):
  res=[]
  for j in range(cot):
    tmp=[]
    for i in range(hang):
      tmp.append(a[i][j])
    res.append(tmp)
  return res  
class Matrix:
  def __init__(self,hang,cot,a):
    self.hang=hang
    self.cot=cot
    self.a=a
    self.chuyenvi=chuyenvi(self.a,self.hang,self.cot)
  def tich(self):
    mang=[]
    for i in range(hang):
      tmp=[]
      for j in range(hang):
        sum=0
        for k in range(cot):
          sum+=self.a[i][k]*self.chuyenvi[k][j]
        tmp.append(sum)
      mang.append(tmp)  
    return mang  
t=int(input())
while(t):
  t-=1
  hang,cot=[int(x) for x in input().split()]
  a=[]
  for i in range(hang):
    list=[int(x) for x in input().split()]
    a.append(list)
  ds = Matrix(hang,cot,a)
  mang = chuyenvi(a,hang,cot)
  res = ds.tich()
  for i in range(hang):
    for j in range(hang):
      print(res[i][j],end=" ")
    print()  
    
  
  