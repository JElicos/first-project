from Library import Library


def searchBooks(library):
    title = input("책 제목을 입력하세요. 모르면 Enter를 누르세요: ").strip()
    author = input("저자를 입력하세요. 모르면 Enter를 누르세요: ").strip()

    if title == "" and author == "":
        print("책 제목이나 저자 중 하나는 입력해야 합니다.")
        return []

    if title == "":
        title = None

    if author == "":
        author = None

    return library.searchBook(title, author)


def selectSerialNumber(results):
    try:
        serialNumber = int(input("책의 시리얼 번호를 입력하세요: "))
    except ValueError:
        print("시리얼 번호는 숫자로 입력해야 합니다.")
        return None

    for book in results:
        if book.serialNumber == serialNumber:
            return serialNumber

    print("검색 결과에 없는 시리얼 번호입니다.")
    return None


def main():
    library = Library()

    while True:
        print()
        print("===== 도서 관리 프로그램 =====")
        print("1. 책 추가")
        print("2. 책 검색")
        print("3. 책 대출")
        print("4. 책 반납")
        print("5. 책 삭제")
        print("0. 프로그램 종료")

        menu = input("메뉴를 선택하세요: ").strip()
        print()

        if menu == "1":
            title = input("책 제목: ").strip()
            author = input("저자: ").strip()
            publisher = input("출판사: ").strip()

            if title == "" or author == "" or publisher == "":
                print("제목, 저자, 출판사를 모두 입력해야 합니다.")
                continue

            library.addBook(title, author, publisher)

        elif menu == "2":
            searchBooks(library)

        elif menu == "3":
            results = searchBooks(library)

            if len(results) == 0:
                continue

            serialNumber = selectSerialNumber(results)

            if serialNumber is None:
                continue

            borrower = input("대여자 이름을 입력하세요: ").strip()

            if borrower == "":
                print("대여자 이름을 입력해야 합니다.")
                continue

            library.borrowBook(serialNumber, borrower)

        elif menu == "4":
            results = searchBooks(library)

            if len(results) == 0:
                continue

            serialNumber = selectSerialNumber(results)

            if serialNumber is None:
                continue

            library.returnBook(serialNumber)

        elif menu == "5":
            results = searchBooks(library)

            if len(results) == 0:
                continue

            serialNumber = selectSerialNumber(results)

            if serialNumber is None:
                continue

            library.removeBook(serialNumber)

        elif menu == "0":
            print("프로그램을 종료합니다.")
            break

        else:
            print("올바른 메뉴 번호를 입력하세요.")


if __name__ == "__main__":
    main()
