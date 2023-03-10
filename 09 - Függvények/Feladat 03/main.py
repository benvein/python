from os import system 
from consoleio import *
from metfunction import *

system("cls")

name: str = None
eletkor: int = None
currentDate: int = 2023

name = getNameFromConsole()
year = getYearFromConsole()

eletkor = currentAge(year, currentDate)
printToConsole(eletkor, name)  
