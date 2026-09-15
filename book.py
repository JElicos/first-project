class Book:
    def __init__(self, title, author, publisher):
        self.title = title
        self.author = author
        self.publisher = publisher

    def show(self):
        print("Name:",self.title)
        print("Author:",self.author)
        print("Publisher:",self.publisher)