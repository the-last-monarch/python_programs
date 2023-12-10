class Libary:
    def __init__(self, ListofBooks):
        self.books = ListofBooks
    
    def displayAvailableBooks(self):
        print("Books avilable in the libary are: ")
        for book in self.books:
            print("*" + book)
        
    def borrowBook(self, bookName):
        if bookName in self.books:
            print(f"You have been issued {bookName}, and keep it safe.")
            self.books.remove(bookName)
            return True
        else:
            print("This book is either not avilable or already issued by someone else. Wait until the book is avilable.")
            return False
        
    def returnBook(self, bookName):
        self.books.append(bookName)
        
        print("Thanks for return this book, We hope you enjoyed reading this book")

class Student:
    def requestBook(self):
        self.book = input("Enter the name of the book you want to borrow: ")
        return self.book
        
    def returnBook(self):
        self.book = input("Enter the name of the book you want to return: ")
        return self.book

if __name__ == "__main__":
    onlineLibary = Libary(["Eat that Frog", "The Secret", "Power", "Atomic Habits"])
    student = Student()
    # onlineLibary.displayAvailableBooks()
    
    while(True):
        welcomeMessage = '''
        \n ----------Welcome to Online Libary(SHADOW)----------
        Choose any option:
        1. To see all avilable books in libary
        2. To request any book 
        3. To return or add a book
        4. Exit
        '''
        #SHADOW
        print(welcomeMessage)
        a = int(input("Enter your choice: "))
        if a == 1:
            onlineLibary.displayAvailableBooks()
        elif a == 2:
            onlineLibary.borrowBook(student.requestBook())
        elif a == 3:
            onlineLibary.returnBook(student.returnBook())
        elif a == 4:
            exit()
        else:
            print("Invalid Choice")