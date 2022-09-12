import math
class PhanSo:
  def __init__(self,tu,mau):
    self.tu=tu
    self.mau=mau
  def rutgon(self):
    x= math.gcd(self.mau,self.tu)
    self.tu=self.tu//x
    self.mau=self.mau//x
  def inkq(self):
    print("{}/{}".format(self.tu,self.mau))
if __name__=='__main__':
  a=[int(x) for x in input().split()]
  ps = PhanSo(a[0],a[1])
  ps.rutgon()
  ps.inkq()
    
    