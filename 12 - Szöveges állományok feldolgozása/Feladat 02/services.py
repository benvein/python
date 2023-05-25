from typing import *
from book import Book

def itBooks(books: List[Book], itTheme: str) -> List[Book]:
    bookIT: List[Book] = []

    for book in books:
        if(book.theme == itTheme):
            bookIT.append(book)

    return bookIT

def booksFrom1900(books: List[Book], book1900: int, book2000: int) -> List[Book]:
    bookFrom20thCentury: List[Book] = []

    for book in books:
        for book in range(book1900, book2000, 1):
            bookFrom20thCentury.append(book)
            
    return bookFrom20thCentury