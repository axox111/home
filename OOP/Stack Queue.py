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
            self.values = self.values[0:self.size]
            self.size -= 1
        
    def public(self):
        volume = self.size + 1
        return volume
        
        
class Queue:
    
    
    def __init__(self):
        self.values = []
        self.size = -1

    def push(self, val):
       self.values = [val] + self.values
       self.size += 1
       
    def pop(self):
        if self.size == -1:
            print('Список пуст. Нечего удалять')
        else:
            self.values = self.values[0:self.size]
            self.size -= 1
        
    def public(self):
        volume = self.size + 1
        return volume

