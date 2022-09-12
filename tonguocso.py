prime = [0]*2000005
d = [0]*2000005


def snt():
    global prime
    global d
    for i in range(2, 2000006):
        prime[i] = 1
    for i in range(2, 2000006):
        if (prime[i] == 1):
            for j in range(2, 2000006):
                k = j
                while (k % i == 0):
                    k //= i
                    d[j] += i
                    prime[j] = 0


n = int(input())
sum = 0
snt()
while (n):
    n -= 1
    p = int(input())
    sum += d[p]
print(sum)
