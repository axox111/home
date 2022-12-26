#367. Даны целые числа a1, a2, a3. Получить целочисленную матрицу [bijh] = 1,2,3. Для которой biJ = ai— 3aj
#Нужно получить матрицу 3х3, в которой каждый элемент считается по формуле bij = ai— 3aj. bij - i - это индекс строки, j - индекс столбца
var1 = 2#int(input("Переменная 1:"))
var2 = 3#int(input("Переменная 2:"))
var3 = 4#int(input("Переменная 3:"))
varList = [var1, var2, var3]
arr = []
size = 3
for i in range(size):
    matrix = []
    for j in range(size):
        matrix.append(varList[i] - 3 * varList[j])
    arr.insert(i, matrix)
print(arr)