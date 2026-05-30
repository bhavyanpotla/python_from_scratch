class Book:
    available = True   

    def __init__(self, title, author):
        self.title = title
        self.author = author
          
    def checkout(self):
        if Book.available==False:
            print(f'"{self.title}" is not available')
        elif Book.available == True:  
            print("book is available and checked out")
            self.available = False  

    def return_book(self):
        if Book.available == False  :
            print(f'"{self.title}" was returned')
            Book.available = True  
        elif Book.available == True:  
            print("book was already returned")


 
b1 = Book("python", "john")
b1.checkout()

b2 = Book("abc", "bgdf")
b2.checkout()   

b1.return_book()
b2.checkout()    

