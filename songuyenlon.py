import math
def reduceB(a, b):
    mod = 0
    for i in range(0, len(b)) :
        mod = (mod * 10 + ord(b[i])-48) % a
    return mod     
def gcdLarge(a, b) :
    num = reduceB(a, b)
    return math.gcd(a, num)
t=int(input())
while(t):
    t-=1
    a=int(input())
    b=str(input())
    if a == 0:
        print(b)
    else:
        print(gcdLarge(a, b))
