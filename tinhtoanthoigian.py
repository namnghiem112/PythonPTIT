import functools

def tru(giovao,giora):
  list1= [int(x) for x in giora.split(":")]
  list2= [int(x) for x in giovao.split(":")]
  gio=0
  phut=0
  if(list1[1]>list2[1]):
    phut = list2[1]+60-list1[1]
    list2[0]-=1
  else: 
    phut = list2[1]-list1[1]
  gio = list2[0]-list1[0]
  res = str(gio)+" "+str(phut)
  return res
def cmp(a,b):
  if(a.gio>b.gio): return -1
  elif(a.gio==b.gio):
    if(a.phut>b.phut): return -1
    else: return 1
  else: return 1
class Time():
  def __init__(self,ma,ten,giora,giovao,gio,phut):
    self.ma=ma
    self.ten=ten
    self.giora=giora
    self.giovao=giovao
    res = tru(self.giovao,self.giora)
    self.gio,self.phut=[int(x) for x in res.split()]
n=int(input())
a=[]
for i in range(n):
  gio=int()
  phut=int()
  ma=str(input())
  ten=str(input())
  giovao=str(input())
  giora=str(input())
  ds = Time(ma,ten,giovao,giora,gio,phut)
  a.append(ds)
a = sorted(a, key = functools.cmp_to_key(cmp))  
for i in a:
  print(i.ma+" ",i.ten,i.gio,"gio",i.phut,"phut")
    