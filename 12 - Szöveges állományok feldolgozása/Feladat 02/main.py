from typing import *
from book import Book
from services import *
from bookIO import *

fileName: str = "data/adatok.txt"
books: List[Book] = readBooksFromFile(fileName)

#Írjuk ki a képernyőre az össz adatot
writeToConsole(books)



#Keressük ki az informatika témajú könyveket és mentsük el őket az informatika.txt állömányba
bookIT: List[Book] = itBooks(books, "informatika")
writeBooksInFile(bookIT, "informatika.txt")



#Az 1900.txt állományba mentsük el azokat a könyveket amelyek az 1900-as években íródtak
booksFrom20thCentury: List[Book] = booksFrom1900(books)
writeBooksInFile(booksFrom20thCentury, "1900.txt")




#Rendezzük az adatokat a könyvek oldalainak száma szerint csökkenő sorrendbe és a sorbarakott.txt állományba mentsük el.
sortBooksByPageNumberDescending(books)
writeBooksInFile(books, "sorbarakott.txt")
