class Sophuc:
  def __init__(self,thuc,ao):
    self.thuc=thuc
    self.ao=ao
  def tong(self,p):
    x = self.thuc+p.thuc
    y = self.ao+p.ao
    return [x]+[y]
  def tich(self,p):
    a,b,c,d = self.thuc,self.ao,p.thuc,p.ao
    x = a*c-b*d
    y = a*d+b*c
    return [x]+[y]
t=int(input())
while(t):
  t-=1
  a=[int(x) for x in input().split()]
  A=Sophuc(a[0],a[1])
  B=Sophuc(a[2],a[3])
  res = A.tong(B)
  sum = Sophuc(res[0],res[1])
  C = sum.tich(A)
  D = sum.tich(sum)
  kytu1=""
  kytu2=""
  if(C[1]<0): kytu1="-"
  else: kytu1="+"  
  if(D[1]<0): kytu2="-"
  else: kytu2="+"
  print("{} {} {}i, {} {} {}i".format(C[0],kytu1,abs(C[1]),D[0],kytu2,abs(D[1])))