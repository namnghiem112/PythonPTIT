n=int(input())
test = int()
list = [int(x) for x in input().split(" ")]
def kt(list):
  for i in range(0,len(list)-1):
    if(list[i]==0): continue
    if (list[i]+list[i+1])%2==0:
      list[i]=0
      list[i+1]=0
  list1 = [int(k) for k in list if k!=0]
  test=1
  list= list1.copy()
  # for i in range(0, len(list)):
  #   print(list[i])
  for i in range(0,len(list)-1):
    if (list[i]+list[i+1])%2==0:
      test=0
  if(test==1):
    print (len(list));
    return
  kt(list)
kt(list)