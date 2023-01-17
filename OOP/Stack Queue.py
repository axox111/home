class Stack:

    
    def __init__(self):
        self.list = []
        
    def push(self, val):
        self.list.append(val)
    
    def pop(self):
        self.list.pop()
        

class Queue:
    
    
    def __init__(self):
        self.list = []
        
    def push(self, val):
        self.list.append(val)
    
    def pop(self):
        self.list.pop(0)