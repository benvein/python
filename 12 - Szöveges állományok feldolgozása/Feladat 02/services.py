from typing import *
from book import Book

def itBooks(books: List[Book], itTheme: str) -> List[Book]:
    bookIT: List[Book] = []

    for book in books:
        if(book.theme == itTheme):
            bookIT.append(book)

    return bookIT