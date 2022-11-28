#296-2 Даны действительные числа а1 ..., а20 (все числа попарно различны).
#Поменять в этой последовательности местами:
#а) наибольший и наименьший члены;
#б) наибольший и последний члены.
import random

var_list = random.sample(range(1, 100), 5)
print("список чисел:", var_list)
highest = 0 
lowest = 0
for i in range(1, len(var_list)):
    if var_list[i] > var_list[highest]:
        highest = i
    if var_list[i] < var_list[lowest]:
        lowest = i
var_list[highest], var_list[lowest] = var_list[lowest], var_list[highest]
print("задание а)", var_list)
var_list[highest], var_list[lowest] = var_list[lowest], var_list[highest]
var_list[highest], var_list[-1] = var_list[-1], var_list[highest]
print("задание б)", var_list)