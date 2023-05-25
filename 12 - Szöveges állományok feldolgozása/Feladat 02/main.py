from typing import *
from book import Book
from services import *
from bookIO import *

books: List[Book] = readBooksFromFile()

#Írjuk ki a képernyőre az össz adatot
print("minden adat: ")
for book in books:
    print(book)



#Keressük ki az informatika témajú könyveket és mentsük el őket az informatika.txt állömányba
bookIT: List[Book] = itBooks(books, "informatika")
writeItBooksInFile(bookIT, "informatika.txt")



#Az 1900.txt állományba mentsük el azokat a könyveket amelyek az 1900-as években íródtak
booksFrom20thCentury: List[Book] = booksFrom1900(books, 1900, 2000)
write1900BooksInFile(booksFrom20thCentury, "1900.txt")




#Rendezzük az adatokat a könyvek oldalainak száma szerint csökkenő sorrendbe és a sorbarakott.txt állományba mentsük el.

