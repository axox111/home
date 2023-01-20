class Animal:
    
    
    def __init__(self, food, location):
        self.food = food
        self.location = location
        
    def makeNoise(self):
        pass
    
    def eat(self):
        pass
    
    def sleep(self):
        print(f"{self.__class__.__name__} спит")


class Dog(Animal):
    
    
    def __init__(self, food, location, friendship):
        self.food = food
        self.location = location
        self.friendship = friendship
    
    def makeNoise(self):
        print(f"{__class__.__name__} делает гав-гав")
        
    def eat(self):
        print(f"{__class__.__name__} ест {self.food}")
    

class Cat(Animal):
    
    
    def __init__(self, food, location, murAbillity):
        self.food = food
        self.location = location
        self.murAbillity = murAbillity

    def makeNoise(self):
        print("{__class__.__name__} делает мав-мав")
    
    def eat(self):
        print(f"{__class__.__name__} ест {self.food}") 
    
    
class Horse(Animal):
    
    
    def __init__(self, food, location, tsokAbillity):
        self.food = food
        self.location = location
        self.tsokAbillity = tsokAbillity

    def makeNoise(self):
        print("{__class__.__name__} делает иго-го")
        
    def eat(self):
        print(f"{__class__.__name__} ест {self.food}")
        
        
class Veterinarian:
    
    
    def __init__(self):
        pass        
    
    def treatAnimal(self, Animal):
        self.animal = Animal
        print(f'Ветеринар лечит {Animal.__class__.__name__} во {Animal.location} настойкой {Animal.food}')
        
    def main(self, *Animal):
        for i in Animal:
            public = i.__class__.__name__
            print(public)

vet = Veterinarian()
dog1 = Dog('Мясо', 'Двор', 'Всегда рад видеть тебя!')
dog2 = Dog('Рыба', 'Пляж', 'Всегда рад видеть меня!')
dog3 = Dog('Кость', 'Мясокомбинат', 'Всегда рад видеть всех!')
cat1 = Cat('Молочко', 'Молокозавод', 'мурррр')
cat2 = Cat('Вискас', 'Дом', 'мур-мур-мур-мур')
cat3 = Cat('Китекет', 'Магазин', 'ммммммммррррррррр')
horse1 = Horse('Сахарок', 'Стойло', 'цок. цок. цок. цок.')
horse2 = Horse('Сено', 'Пастбище', 'цокцокцокцокцок')
horse3 = Horse('Рожь', 'Поле', 'цок! цок-цок! цок-цок-цок-цок-цок-цок')
vet.main(dog1, cat1, horse1)
vet.treatAnimal(dog1)