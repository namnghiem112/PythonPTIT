import math
class bangDiem:
  def __init__(self,ma,ten,tongdiem):
    self.ma=ma
    self.ten=ten    
    self.tongdiem=tongdiem
    if(self.tongdiem>=9): self.hanhkiem="XUAT SAC"
    elif(self.tongdiem>=8): self.hanhkiem="GIOI"
    elif(self.tongdiem>=7): self.hanhkiem="KHA"
    elif(self.tongdiem>=5): self.hanhkiem="TB"
    else: self.hanhkiem="YEU"

n=int(input())
a=[]
for i in range(1,n+1):
  ten=str(input())
  list=[float(x) for x in input().split()]
  tongdiem=round((sum(list)+list[0]+list[1])/10/1.2,1)
  ds=bangDiem(i,ten,tongdiem)
  a.append(ds)
a=sorted(a,key=lambda x:x.tongdiem,reverse=True) 
for i in range(0,n):
  if(a[i].ma <10): a[i].ma="HS0"+str(a[i].ma)
  else: a[i].ma="HS"+str(a[i].ma)
  print("{} {} {:.1f} {}".format(a[i].ma,a[i].ten,a[i].tongdiem,a[i].hanhkiem))

  