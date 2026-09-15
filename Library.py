import json

from book import Book


class Library:
    def __init__(self, dataFile="LibData.txt"):
        self.dataFile = dataFile
        self.books = []
        self.loadBooks()

    def loadBooks(self):
        try:
            with open(self.dataFile, "r", encoding="utf-8") as file:
                data = file.read().strip()

            if data == "":
                return

            savedBooks = json.loads(data)

            for savedBook in savedBooks:
                book = Book(savedBook["title"], savedBook["author"])
                book.publisher = savedBook["publisher"]
                book.serialNumber = savedBook["serialNumber"]
                book.isBorrowed = savedBook["isBorrowed"]
                book.borrower = savedBook["borrower"]
                self.books.append(book)

        except FileNotFoundError:
            return
        except json.JSONDecodeError:
            print("도서 데이터 파일의 형식이 올바르지 않습니다.")

    def saveBooks(self):
        savedBooks = []

        for book in self.books:
            savedBooks.append(
                {
                    "title": book.title,
                    "author": book.author,
                    "publisher": book.publisher,
                    "serialNumber": book.serialNumber,
                    "isBorrowed": book.isBorrowed,
                    "borrower": book.borrower,
                }
            )

        with open(self.dataFile, "w", encoding="utf-8") as file:
            json.dump(savedBooks, file, ensure_ascii=False, indent=4)

    def makeSerialNumber(self):
        if len(self.books) == 0:
            return 1

        largestNumber = 0

        for book in self.books:
            if book.serialNumber > largestNumber:
                largestNumber = book.serialNumber

        return largestNumber + 1

    def addBook(self, title, author, publisher):
        book = Book(title, author)
        book.publisher = publisher
        book.serialNumber = self.makeSerialNumber()
        book.isBorrowed = False
        book.borrower = None

        self.books.append(book)
        self.saveBooks()

        print("책이 저장되었습니다.")
        return book

    def searchBook(self, title=None, author=None):
        results = []

        for book in self.books:
            titleMatches = title is None or title.lower() in book.title.lower()
            authorMatches = author is None or author.lower() in book.author.lower()

            if titleMatches and authorMatches:
                results.append(book)

        if len(results) == 0:
            print("검색 결과가 없습니다.")
            return results

        for book in results:
            print(
                "시리얼 번호:",
                book.serialNumber,
                "/ 제목:",
                book.title,
                "/ 저자:",
                book.author,
                "/ 출판사:",
                book.publisher,
            )

        return results

    def findBookBySerialNumber(self, serialNumber):
        for book in self.books:
            if book.serialNumber == serialNumber:
                return book

        return None

    def removeBook(self, serialNumber):
        book = self.findBookBySerialNumber(serialNumber)

        if book is None:
            print("해당 시리얼 번호의 책이 없습니다.")
            return False

        self.books.remove(book)
        self.saveBooks()

        print("책이 삭제되었습니다.")
        return True

    def borrowBook(self, serialNumber, borrower):
        book = self.findBookBySerialNumber(serialNumber)

        if book is None:
            print("해당 시리얼 번호의 책이 없습니다.")
            return False

        if book.isBorrowed:
            print("이미 대출된 책입니다.")
            return False

        book.isBorrowed = True
        book.borrower = borrower
        self.saveBooks()

        print("대출 처리되었습니다.")
        return True

    def returnBook(self, serialNumber):
        book = self.findBookBySerialNumber(serialNumber)

        if book is None:
            print("해당 시리얼 번호의 책이 없습니다.")
            return False

        if not book.isBorrowed:
            print("대출 중인 책이 아닙니다.")
            return False

        book.isBorrowed = False
        book.borrower = None
        self.saveBooks()

        print("반납 처리되었습니다.")
        return True
