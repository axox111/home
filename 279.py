#279Даны действительные числа а1, ..., аn, b1, ..., bn.
#вычислить (a1 + bn) * (a2 - bn-1) * ... * (an + b1)
import random

var_number = int(input("введите количество чисел: "))
max_range = 100
a = random.sample(range(1, max_range), var_number)
b = random.sample(range(1, max_range), var_number)
i = 0
res = 1
while i < len(a):
    sum = a[i] + b[var_number - i - 1]
    res *= sum
    i +=1
print(a)
print(b)
print(res)