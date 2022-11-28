#296 Даны действительные числа а1 ..., а20 (все числа попарно различны).
#Поменять в этой последовательности местами:
#а) наибольший и наименьший члены;
#б) наибольший и последний члены.
import random

def min_list_value(x):
    temp_list = x[:]
    temp_list.sort()
    return temp_list[0]

def max_list_value(x):
    temp_list = x[:]
    temp_list.sort()
    return temp_list[len(temp_list) - 1]

max_range = 100
var_number = 20
a = random.sample(range(1, max_range), var_number)
ab = a[:]
min_value = min_list_value(a)
max_value = max_list_value(a)
index_min = a.index(min_value)
index_max = a.index(max_value)
print("список дейсвительных чисел = ", a)
print("минимальное число = ", min_value,", индекс числа =", a.index(min_value))
print("максимальное число = ", max_value, ", индекс числа =", a.index(max_value))
a[index_min], a[index_max] = a[index_max], a[index_min]
print("задание а)", a)
ab[len(ab) - 1], ab[index_max] = ab[index_max], ab[len(ab) - 1]
print("задание б)", ab)