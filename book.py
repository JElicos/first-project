class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.isBorrowed =  False
        self.borrower = None

    def show(self):
        print("Name:",self.title)
        print("Author:",self.author)
        if self.isBorrowed == True:
            return 
        print("Borrower:",self.borrower)