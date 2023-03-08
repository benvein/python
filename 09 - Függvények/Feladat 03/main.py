from os import system 
system("cls")
from consoleio import *
from metfunction import *

eletkor: int = None

name: str = getNameFromConsole()
eletkor = currentAge(year)
printToConsole(eletkor, name)
