#Сортировка пУзЫрЬКоМ
import random

size_of_list = 20
x = [random.randint(1, 100) for x in range(size_of_list + 1)]
count = 0
for j in range(len(x) - 2):
    for i in range(len(x) - 1):
        if x[i] > x[i + 1]:
            x[i], x[i + 1] = x[i + 1], x[i]     
            count += 1
print(f"количество перестановок {count}")
print(f"отсоротированный список по возрастанию {x}")