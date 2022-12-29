class Reader:

    def __init__(self, fullName, ticketNumber, faculty,
                 birthDate, phoneNumber):
        self.fullName = fullName
        self.ticketNumber = ticketNumber
        self.faculty = faculty
        self.birthDate = birthDate
        self.phoneNumber = phoneNumber  
    
    def takeBook(self, takenBooks):
        if isinstance(takenBooks, int):
            print(f"{self.fullName} взял {takenBooks} книг(и)")
        elif isinstance(takenBooks, str):
            print(f"{self.fullName} взял {takenBooks}")
        elif isinstance(takenBooks, Book):
            print(f"{self.fullName} взял {takenBooks.bookName}, {takenBooks.bookAuthor}")

    def returnBook(self, returnBooks):
        if isinstance(returnBooks, int):
            print(f"{self.fullName} вернул {returnBooks} книг(и)")
        elif isinstance(returnBooks, str):
            print(f"{self.fullName} вернул{returnBooks}")
        elif isinstance(returnBooks, Book):
            print(f"{self.fullName} вернул {returnBooks.bookName}, {returnBooks.bookAuthor}")
            
class Book:
    
    def __init__(self, bookName, bookAuthor):
        self.bookName = bookName
        self.bookAuthor = bookAuthor
        
reader1 = Reader('Петров В.В.', 'безумно можно быть пеееервым',
                 'Добрососедство', '28.12.1990', '88005553535')      
book1 = Book('50 оттенков серого', 'Гена Букин')

reader1.takeBook(3)
reader1.takeBook('Пушкин, Есенина и Погулять')
reader1.takeBook(book1)
reader1.returnBook(3)
reader1.returnBook('Пушкин, Есенина и Погулять')
reader1.returnBook(book1)
                                    