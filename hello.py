def chuyen(a,b):
  res = (a+b)/2
  while(res >=10):
    res/=10
  return res  
def xeploai(a):
  res=""
  if(a<5): res="TRUOT"
  elif(a<8): res="CAN NHAC"
  elif(a<9.5): res="DAT"  
  else: res="XUAT SAC"
  return res  
class Nhanvien:
  def __init__(self,ma,ten,diemlt,diemth):
    self.ma=ma
    self.ten=ten
    self.diemlt=diemlt
    self.diemth=diemth
    self.tong = chuyen(self.diemlt,self.diemth)
    self.loai = xeploai(self.tong)
n=int(input())
a=[]
for i in range(1,n+1):
  ten=str(input())
  diemlt=float(input())
  diemth=float(input())
  ds = Nhanvien(i,ten,diemlt,diemth)
  a.append(ds)
a=sorted(a,key=lambda x:x.tong,reverse=True) 
for i in range(0,n):
  if(a[i].ma <10): a[i].ma="TS0"+str(a[i].ma)
  else: a[i].ma="TS"+str(a[i].ma)
  print("{} {} {:.2f} {}".format(a[i].ma,a[i].ten,a[i].tong,a[i].loai))
  