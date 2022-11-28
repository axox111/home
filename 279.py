#279Даны действительные числа а1, ..., аn, b1, ..., bn.
#вычислить (a1 + bn) * (a2 - bn-1) * ... * (an + b1)
import random

var = int(input("введите количество чисел: "))
max_range = 100
a = random.sample(range(1, max_range), var)
b = random.sample(range(1, max_range), var)
i = 0
res = 1
b.reverse()
while i < var:
    sum = a[i] + b[i]
    res *= sum
    i +=1
print(a)
print(b)
print(res)