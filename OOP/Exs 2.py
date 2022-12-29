class Person:
   
    
    def __init__(self, fullName = 'unnamed', age = 'N/A'):
        self.fullName = fullName
        self.age = age
        
    def move(self):
        print(f"{self.fullName} говорит")
    
    def talk(self):
        print(f"{self.fullName} говорит")  
    
anon = Person()
vova = Person('vova', 10)
print(anon.fullName, anon.age)
print(vova.fullName, vova.age)
anon.move()
vova.talk()