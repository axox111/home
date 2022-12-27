import random

def creatematrix(rows, columns):
    arr = []
    for i in range(rows):
        i = [random.randrange(100) for x in range(columns)]
        arr.append(i)
    return arr

def simplelst(array):
    temp = []
    for i in array:
        for j in i:
            temp.append(j)
    return temp

def sumMatrix(arr1, arr2):
    a = simplelst(arr1)
    b = simplelst(arr2)
    temp_sum = []
    for i in range(len(a)):
        temp_sum.append(a[i] + b[i])
    return temp_sum
    
rows = 3
columns = 3
res = []
a = creatematrix(rows, columns)
b = creatematrix(rows, columns)
print(a)
print(b)
summary = sumMatrix(a,b)
for i in range(columns):
    temp_res = []
    for j in range(columns):
        temp_res.append(summary[0])
        summary.pop(0)
        
    res.insert(i, temp_res)       
    
print(res)
    