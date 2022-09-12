def chuyen(a, b, num1, num2):
    if (a < b):
        a, b = b, a
    a = str(a)
    b = str(b)
    res1 = num1.replace(a, b)
    res2 = num2.replace(a, b)
    res3 = int(int(res1)+int(res2))
    res4 = num1.replace(b, a)
    res5 = num2.replace(b, a)
    res6 = int(int(res4)+int(res5))
    print(res3,res6)
t = int(input())
while (t):
    t -= 1
    a, b = input().split()
    num1 = input().strip()
    if(num1.count(' ')):num1, num2 = num1.split()
    else: num2 = input()
    chuyen(a, b,num1, num2)