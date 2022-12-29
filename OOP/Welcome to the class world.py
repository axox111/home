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
       

samsung = Phone(88005553535, 'Samsung', 412)
apple = Phone(77009379992, 'Apple', 200)
nokia = Phone(797822211166, 'Nokia', 600)
print(samsung.number, samsung.model, samsung.weight)
print(apple.number, apple.model, apple.weight)
print(nokia.number, nokia.model, nokia.weight)
samsung.getNumber
samsung.receiveCall('Кельфаен', '%anyGeorgiaNumber%')
samsung.sendMessage('8800111111, 6600656666, 770055555')