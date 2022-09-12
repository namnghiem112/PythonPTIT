from math import factorial
n, k = [int(x) for x in input().split()]
if 1 <= k <= n <= 25:
  c = factorial(n)/(factorial(k)*factorial(n-k))
print(int(c))