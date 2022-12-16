import random
import time

n = int(input('Введите желаемое число списка:'))
a_min = 1
a_max = 10000
start = time.time()
numbers = [random.randint(a_min, a_max) for x in range(n)] 
lst_of_numbers = ''
file_bbl = open('sort by BUUBLES.txt', 'w')
for j in range(len(numbers)): 
    counter = 0
    for i in range(len(numbers)- 1): 
        if numbers[counter] > numbers[counter + 1]:
            numbers[counter], numbers[counter + 1] = numbers[counter + 1], numbers[counter]
        counter +=1
lst_of_numbers = str(numbers)        
file_bbl.write(lst_of_numbers)
file_bbl.close()
end = time.time()
print(f"{round(end - start, 2)} сек.")
#O(N) + #O(N ** 2) - 1