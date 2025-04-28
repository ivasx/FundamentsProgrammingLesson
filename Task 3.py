class Book:
    def __init__(self, title, author, price):
        self.__title = title
        self.__author = author
        self.__price = price

    def set_title(self, title):
        self.__title = title

    def set_author(self, author):
        self.__author = author

    def set_price(self, price):
        self.__price = price

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def get_price(self):
        return self.__price

if __name__ == '__main__':
    book1 = Book('George Orwell', '1984', 300)
    book2 = Book('J.K. Rowling', 'Harry Potter', 500)
    book3 = Book('J.R.R. Tolkien', 'The Hobbit', 400)

    print(book1.get_title())
    print(book1.get_author())
    print(book1.get_price())
    book1.set_price(450)
    print(book1.get_price())