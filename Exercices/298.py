# 298. Даны целые числа а1 ..., а25, b1, ..., b25.
#Преобразовать последовательность b1 ..., b25 по правилу:
#если ai <= 0, то bi увеличить в 10 раз, 
#иначе bi заменить нулем (i = 1, 25)
import random

i = 25
min_range = -100
max_range = 100
a = random.sample(range(min_range, max_range + 1), i)
b = random.sample(range(min_range, max_range + 1), i)
print(a)
print(b)
for i in range(0, len(a)):
    if a[i] <= 0:
        b[i] = b[i] * 10
    else:
        b[i] = b[i] * 0
print(b)