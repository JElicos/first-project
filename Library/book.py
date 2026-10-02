class Book:


    def __init__(self, title, author, publisher,isbn,quantity,price):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.quantity = quantity
        self.price = price

    def reprint(self,quantity): #quantity 만큼 인쇄
        return None
        

    def sell(self,quantity):

        
    
    def show(self):
        print("Name:",self.title)
        print("Author:",self.author)
        print("ISBN:",self.isbn)
        print('Price:',self.price)