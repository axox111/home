#373. Даны натуральное число n, действительная матрица размера nх9. Найти среднее арифметическое:
#а) каждого из столбцов;
import random
n = int(input("Данное натуральное число:"))
column = 9
matrix = []
while n > 0:
    matrix.append([random.randrange(1, 100) for x in range(column)])
    n -= 1
print(matrix)
for column_number in range(column):
    column_sum = 0
    for line in matrix:
        column_sum += line[column_number]
    avg = column_sum / len(matrix)
    print(f"среднее арифметическое {column_number + 1} столбца - {round(avg, 2)}")