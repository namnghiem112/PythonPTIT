import math
from decimal import Decimal


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, k):
        x0 = self.x - k.x
        y0 = self.y - k.y
        f = math.sqrt(x0 * x0 + y0 * y0)
        return f


def check(self, a, b):
    if (self + b > a and self + a > b and a + b > self): return 1
    return 0


class Triangle(Point):
    def __init__(self, x, y):
        super().__init__(x, y)

    def tong(self, d1, d2):
        a = self.distance(d1)
        b = self.distance(d2)
        c = d1.distance(d2)
        if (check(a, b, c) == 1): return "{:.3f}".format(a + b + c)
        else: return 0


if __name__ == '__main__':
    t = int(input())
    while t > 0:
        arr = input().split()
        d1 = Triangle(Decimal(arr[0]), Decimal(arr[1]))
        d2 = Triangle(Decimal(arr[2]), Decimal(arr[3]))
        d3 = Triangle(Decimal(arr[4]), Decimal(arr[5]))
        if (d1.tong(d2, d3) != 0): print(d1.tong(d2, d3))
        else: print("INVALID")
        t -= 1
