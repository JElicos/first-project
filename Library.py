import json

from book import Book


class Library:
    def __init__(self,title,author,publisher):
        self.title = title
        self.author = author
        self.publisher = publisher

    def addBook(self,title,author):
        # 1. 책의 이름, 저자, 출판사를 입력받기
        # 2. 데이터베이스에 저장
        # 3. 저장 후 저장되었습니다. 출력

    def removeBook(self,title,author):
        # 1. 삭제하려는 책의 이름이나 저자를 검색
        # 2. 데이터베이스에서 일치하는 목록을 가져와 콘솔에 출력
        #       2-2. 이름 저자 시리얼넘버
        # 3. 선택받고 삭제 후 삭제되었습니다. 출력

    def searchBook(self,title,author):
        #1. 책이나 저자의 이름을 입력받기.
        # 2. 리이브러리에서 데이터를 불러와 콘솔에 츨력
        # 3. 대출 선택지 출력.
        # 4. 이후 borrowed 매서드로 연결
    
    def Borrow(self, title, borrower):
            #1.이름이나 저자를 입력받고
            #2. 데이터베이스의 책 정보와 대조해 출력하고
            # 3. 사용자가 선택한 책이 borroed 인지 체크
            # 4. borrowed 라면 이미 대출된 책입니다. 프린트
            # 5.borrroed 되지 않았다면 사용자의 정보를 입력받은 후 대출처리
            #   5-1 대출처리 후 대출처리 되었습니다. 출력 
