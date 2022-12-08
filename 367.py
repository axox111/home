#367. Даны целые числа a1, a2, a3. Получить целочисленную матрицу [bijh] = 1,2,3. Для которой biJ = ai— 3aj
#Нужно получить матрицу 3х3, в которой каждый элемент считается по формуле bij = ai— 3aj. bij - i - это индекс строки, j - индекс столбца
var1 = 3#int(input("Переменная 1:))
var2 = 7#int(input("Переменная 2:))
var3 = 2#int(input("Переменная 3:))
varList = [var1, var2, var3]
size = 3
matrix = []
for i in range(size):
    for j in range(size):
        matrix.append(varList[i] - 3 * varList[j])
    print(matrix)
    matrix =[]