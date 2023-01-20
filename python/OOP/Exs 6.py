class Car:
    
    
    def __init__(self, model, segment, weight, driverName, engineType):
        self.model = model
        self.segment = segment
        self.weight = weight
        self.driverName = driverName
        self.engineType = engineType
        
    def toString(self):
        print(self.model, self.segment, self.weight, self.driverName, self.engineType)
        
    def start(self):
        print("Поехали!")
    
    def stop(self):
        print("Останавливаемся!")
    
    def turnRight(self):
        print("Поворачиваем направо")

    def turnLeft(self):
        print("Поворачиваем налево")
    

class Lorry(Car):
    def __init__(self, model, segment, weight, driverName, engineType, pickUpPower):
        self.model = model
        self.segment = segment
        self.weight = weight
        self.driverName = driverName
        self.engineType = engineType
        self.pickUpPower = pickUpPower  
        
        
class SportCar(Car):
    def __init__(self, model, segment, weight, driverName, engineType, speedLimit):
        self.model = model
        self.segment = segment
        self.weight = weight
        self.driverName = driverName
        self.engineType = engineType
        self.speedLimit = speedLimit  

    
class Engine:
    
    
    def __init__(self, power, producer):
        self.power = power
        self.producer = producer


class Driver:
    
    
    def __init__(self, fullName, driveExperience):
        self.fullName = fullName
        self.driveExperience = driveExperience

motor = Engine('102', 'PQ1782')
driver = Driver('Ignat', 'Taragrovich')
vesta = Car('Vesta', 'Premium', '1000', driver.fullName, motor.producer)


vesta.toString()
vesta.turnRight()