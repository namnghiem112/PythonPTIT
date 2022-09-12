import functools
import math
def tinhtien(a,b):
  res=0
  if(b-a>=0 and b-a<=50):
    res=math.ceil((b-a)*102)
  elif (b-a>=51 and b-a<=100):
    res=math.ceil((50*100+(b-a-50)*150)*1.03)
  else: res = math.ceil((50*100+50*150+(b-a-100)*200)*1.05)  
  return res  
def cmp(a,b):
  if(a.tong>b.tong): return -1
  else: return 1
class hoaDon:
  def __init__(self,ma,ten,chisomoi,chisocu):
    self.ma=ma
    self.ten=ten
    self.chisomoi=chisomoi
    self.chisocu=chisocu
    self.tong=tinhtien(self.chisomoi,self.chisocu)
n=int(input())
a=[]
for i in range(1,n+1):
  ten=str(input())
  chisocu=int(input())
  chisomoi=int(input())
  ds = hoaDon(i,ten,chisocu,chisomoi)
  a.append(ds)
a = sorted(a, key = functools.cmp_to_key(cmp))    
for i in range(0,n):
  if(a[i].ma <10): a[i].ma="KH0"+str(a[i].ma)
  else: a[i].ma="KH"+str(a[i].ma)
  print(a[i].ma,a[i].ten,a[i].tong)
      