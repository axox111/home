import time
import math

def quick_sort(x):
    if len(x) <= 1:
        return x
    elem = x[0]
    lower = []
    bigger = []
    middle = []
    for i in x:
        if i < elem:
            lower.append(i)
        elif i > elem:
            bigger.append(i)
        else:
            middle.append(i)
    return quick_sort(lower) + middle + quick_sort(bigger)
            
base_file = open('generated list.txt', 'r')
convert_to_list = [int(i) for i in str(base_file.read()).split()]
base_file.close()
start = time.time()
sorted = quick_sort(convert_to_list)
end = time.time() - start
print(f"Сортировка заверешена за {round(end, 2)} сек.")
sorted_file = open('sorted by quick sort.txt', 'w')
value = ''
for i in sorted:
    value = str(i) + ' '
    sorted_file.write(value)
sorted_file.close()
print(f"Сложность сортировки O({round(len(convert_to_list)* math.log2(len(convert_to_list)), 2)})")