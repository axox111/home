import time
import random

a_min = 1
a_max = 100
n = int(input("Введите желаемое число значений:"))
start = time.time()
numbers = [random.randint(a_min, a_max) for x in range(n)]
file_paste = open("sort by paste.txt", 'w')
temp_val = ''
for j in range(1, len(numbers)):
    for i in range(j, 0, -1):
        if numbers[i] < numbers[i - 1]:
            numbers[i], numbers[i - 1] = numbers[i - 1], numbers[i]
        else:
            break
temp_val = str(numbers)
file_paste.write(temp_val)
file_paste.close()
end = time.time() - start
print(f"а этот код занял {round(end, 2)} секунд.")
#O(N **2)