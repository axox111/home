#279Даны действительные числа а1, ..., аn, b1, ..., bn.
#вычислить (a1 + bn) * (a2 - bn-1) * ... * (an + b1)
import random

a = random.sample(range(1, 100), 5)
b = random.sample(range(1, 100), 5)
n = 5
i = 0
res = 1
b.reverse()
while i < n:
    sum = a[i] + b[i]
    res *= sum
    i +=1
print(a)
print(b)
print(res)