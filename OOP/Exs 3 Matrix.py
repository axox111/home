class Matrix:
    
    
    def __init__(self, arr, size):
        self.arr = arr
        self.size = size
        
    def __getitem__(self, index):
        return self.arr[index]
    
    def sumMatrix(self, otherArr):
        if isinstance(otherArr, Matrix):
             res = []
             for i in range(len(self.arr)):
                 temp = []
                 for j in range(len(self.arr)):
                    value = self[i][j] + otherArr[i][j]
                    temp.append(value)
                 res.append(temp) 
        return res
    
    def multiMatrix(self, multiplier):
        if isinstance(multiplier, (int, float)):
             res = []
             for i in range(len(self.arr)):
                 temp = []
                 for j in range(len(self.arr)):
                    value = self[i][j] * multiplier
                    temp.append(value)
                 res.append(temp) 
        return res
    
    
arr1 = [[93, 85, 96], [46, 1, 79], [35, 16, 85]]
arr2 = [[33, 20, 80], [75, 76, 46], [56, 44, 4]]

a = Matrix(arr1, len(arr1))
b = Matrix(arr2, len(arr2))
c = a.sumMatrix(b)
d = a.multiMatrix(4)
print(a.arr)
print(b.arr)
print(c)
print(d)