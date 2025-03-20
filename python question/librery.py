class librery:
        def __init__(self):
                self.books = []
                self.NoBooks = 0 
                
        def addBooks(self, book):
                self.books.append(book)
                self.No_Books = len(self.books)
        
        def show(self) :
                print(f"number of books {self.No_Books}") 
                for b in self.books:
                        print(b)      
l1 = librery()

l1.addBooks('aditya the great')
l1.addBooks('adithe great')
l1.addBooks('aditya  great')
l1.addBooks('the great')
l1.addBooks('aditya ')
l1.addBooks('aditya thet')

l1.show()