from os import system 
system("cls")
from consoleio import *
from metfunction import *

name: str = None
eletkor: int = None
currentDate: int = 2023

name = getNameFromConsole()
year = getYearFromConsole()

eletkor = currentAge(year, currentDate)
printToConsole(eletkor, name)  
