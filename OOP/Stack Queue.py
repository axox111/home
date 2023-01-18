class Stack:

    
    def __init__(self):
        self.values = []
        self.size = -1
        
    def push(self, val):
        self.values += [val]
        self.size += 1
        
    def pop(self):
        if self.size == -1:
            print('Список пуст. Нечего удалять')
        else:
            poped = self.values[-1]
            self.values = self.values[0:self.size]
            self.size -= 1
            print(f"Удаляем {poped}")
        
    def getSize(self):
        volume = self.size + 1
        print(volume)
        
        
class Queue:
    
    
    def __init__(self):
        self.values = []
        self.size = -1

    def push(self, val):
       self.values = self.values + [val]
       self.size += 1
       
    def pop(self):
        if self.size == -1:
            print('Список пуст. Нечего удалять')
        else:
            poped = self.values[-1]
            self.values = self.values[0:self.size]
            self.size -= 1
            print(f"Удаляем {poped}")
        
    def getSize(self):
        volume = self.size + 1
        print(volume)