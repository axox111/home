import random 
import math

class Phone:
    def __init__(self, number, model, weight):
        self.number = number
        self.model = model
        self.weight = weight
        
    def receiveCall(self, callerName, callerNumber):
        print(f"Звонит {callerName}, {callerNumber}")
    
    def getNumber(self):
        print(self.number)
        
    def sendMessage(self,spamContacts):
        print(spamContacts)
        
class Person1:
    def __init__(self, fullName, age):
        self.fullName = fullName
        self.age = age
        
    def talk1(self):
        print(f"{self.fullName} говорит")
        
class Person2:
    def __init__(self):
        pass
    
    def talk2(self):
        print(f"{self.fullName} говорит")
 
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


# samsung = Phone(88005553535, 'Samsung', 412)
# apple = Phone(77009379992, 'Apple', 200)
# nokia = Phone(797822211166, 'Nokia', 600)
# print(samsung.number, samsung.model, samsung.weight)
# print(apple.number, apple.model, apple.weight)
# print(nokia.number, nokia.model, nokia.weight)
# samsung.getNumber
# samsung.receiveCall('Кельфаен', '%anyGeorgiaNumber%')
# samsung.sendMessage('8800111111, 6600656666, 770055555')

# oleg = Person1('Олег', 17)
# gleb = Person2()
# gleb.fullName = 'Глеб'
# gleb.age = '19' 
# oleg.talk1()
# gleb.talk2()