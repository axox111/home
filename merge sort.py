import time
import math

def merge_sort(x):
    if len(x) == 1:
        return x
    else:
        elem = len(x) // 2
        first_list = merge_sort(x[:elem])
        second_list = merge_sort(x[elem:])
        return merge_sorting(first_list, second_list)

def merge_sorting(x, y):
    i = j = 0
    final = []
    while i < len(x) and j < len(y):
        if x[i] < y[j]:
            final.append(x[i])
            i += 1
        else:
            final.append(y[j])
            j += 1
    if i < len(x):
        final += x[i:]
    if j < len(y):
        final += y[j:]
    return final
            
base_file = open('generated list.txt', 'r')
numbers = [int(i) for i in str(base_file.read()).split()]
base_file.close()
start = time.time()
sorting = merge_sort(numbers)
end = time.time() - start
sorted_file = open('sorted by merge.txt', 'w')
for i in sorting:
    sorted_file.write(str(i) + ' ')
sorted_file.close()
print(f"Сортировка слиянием заняла {round(end, 2)} сек")
print(f"сложность алгоритма O({round(len(numbers)*math.log2(len(numbers)), 2)})")