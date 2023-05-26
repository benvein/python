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

   
    return bookFrom20thCentury