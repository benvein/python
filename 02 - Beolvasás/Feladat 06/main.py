from os import system

releaseDate: int = None
director: str = None
movieName: str = None
mainChar: str = None

print("Film cime: ",end="")
movieName = str(input())

print("megjelenes eve: ",end="")
releaseDate = int(input())

print("film rendezoje: ",end="")
director = str(input())

print("foszereplő: ",end="")
mainChar = str(input())

system("cls")

print(f"{releaseDate}-ban/ben {director} rendezésében megjelent a/az {movieName} című film {mainChar} főszereplésével")