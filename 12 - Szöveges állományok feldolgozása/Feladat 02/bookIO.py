from book import Book
from typing import *
import os
from io import open
from datetime import datetime

def readBooksFromFile(fileName: str) -> List[Book]:

    fileName: str = "data/adatok.txt"
    basepath: str = os.path.dirname(os.path.abspath(__file__))
    fileFullPath: str = os.path.join(basepath, fileName)

    oneLine: str = None
    data: List[str] = []
    books: List[Book] = []
    book: Book = None

    try:
        with open(fileFullPath,encoding="utf-8", mode="r") as file:
            for line in file:
                oneLine = line.strip() 
                data = oneLine.split('\t')

                book = Book()
                book.writerFirstName = data[0]
                book.writerLastName = data[1]
                book.writerBirthDate = datetime.fromisoformat(data[2])
                book.bookTitle = data[3]
                book.isbn = data[4]
                book.publsher = data[5]
                book.publishYear = int(data[6])
                book.bookPrice = float(data[7])
                book.theme = data[8]
                book.pageNumbers = int(data[9])
                book.writerMononarium = float(data[10])

                books.append(book)

        return books
    except FileNotFoundError as ex:
        print(f"{ex.filename} nem található!")
        return []

def writeItBooksInFile(books: List[Book], fileName: str) -> None:
    basepath: str = os.path.dirname(os.path.abspath(__file__))
    basepath += "/output"
    fileFullPath: str = os.path.join(basepath, fileName)

    try:
        with open(fileFullPath, encoding="utf-8", mode="w") as file:
            for book in books:
                file.write(f"{book.writerFirstName} {book.writerLastName} - {book.bookTitle} [{book.publishYear}], {book.theme}\n")
    except FileNotFoundError as ex:
        print(f"{ex.filename} nem talalhato")

def write1900BooksInFile(books: List[Book], fileName: str) -> None:
    basepath: str = os.path.dirname(os.path.abspath(__file__))
    basepath += "/output"
    fileFullPath: str = os.path.join(basepath, fileName)

    try:
        with open(fileFullPath, encoding="utf-8", mode="w") as file:
            for book in books:
                file.write(f"{book.writerFirstName} {book.writerLastName} - {book.bookTitle} [{book.publishYear}], {book.theme}\n")
    except FileNotFoundError as ex:
        print(f"{ex.filename} nem talalhato")