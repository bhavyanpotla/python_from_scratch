class Book:
    available = True   

    def __init__(self, title, author):
        self.title = title
        self.author = author

    def checkout(self):
        if Book.available:
            Book.available = False
            print(f'"{self.title}" has been checked out')
        else:
            print("No books are available right now")

    def return_book(self):
        if not Book.available:
            Book.available = True
            print(f'"{self.title}" has been returned')
        else:
            print("Books are already available")


 
b1 = Book("python", "john")
b1.checkout()

b2 = Book("abc", "bgdf")
b2.checkout()   

b1.return_book()
b2.checkout()    