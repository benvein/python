from typing import *
from book import Book

def writeToConsole(books: List[Book]) -> None:
    for book in books:
        print(book)

def itBooks(books: List[Book], itTheme: str) -> List[Book]:
    bookIT: List[Book] = []

    for book in books:
        if(book.theme == itTheme):
            bookIT.append(book)

    return bookIT

def booksFrom1900(books: List[Book]) -> List[Book]:
    bookFrom20thCentury: List[Book] = []

    for book in books:
        if (1900<book.publishYear and book.publishYear<2000):
            bookFrom20thCentury.append(book)

    return bookFrom20thCentury

def sortBooksByPageNumberDescending(books: List[Book]) -> None:
    booksCount: int = len(books)
    temp: Book = None

    for i in range(0, booksCount-1, 1):
        for j in range(i+1, booksCount):
            if (books[j].pageNumbers > books[i].pageNumbers):
                temp = books[i]
                books[i] = books[j]
                books[j] = temp
    