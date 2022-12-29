class Student:
    
    
    def __init__(self, firstName, lastName, group, averageMark):
        self.firstName = firstName
        self.lastName = lastName
        self.group = group
        self.averageMark = averageMark
    
    def getScholarship(self):
        if self.averageMark == 5:
            print("Степендия 100")
        else:
            print("Степендия 80")
        
    
class Aspirant(Student):
    
    
    def __init__(self, firstName, lastName, group, averageMark, degree):
        self.firstName = firstName
        self.lastName = lastName
        self.group = group
        self.averageMark = averageMark
        self.degree = degree        
    
    def getScholarship(self):
        if self.averageMark == 5:
            print("Степендия 200")
        else:
            print("Степендия 180")


student = Student('Ivan', 'Hlebov', 'Group 2', 4.75)
best_student = Student('Hypa', 'Shamanovich', 'Heroes of Azeroth', 5)
aspirant = Aspirant('Yana', 'Molodozhonovna', 'Krovi', 4.4, 'Bachelor')
best_aspirant = Aspirant('Silvana', 'Rynn', 'Forsaken', 5, 'Chief')

student.getScholarship()
best_student.getScholarship()
aspirant.getScholarship()
best_aspirant.getScholarship()
best_aspirant.degree

