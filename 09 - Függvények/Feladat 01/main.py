from os import system
system("cls")
from metfunctions import *
from consoleio import *

x: float = None
y: float = None
result: float = None

x = getNumberFromConsole()
y = getNumberFromConsole()

result = sumOfTwoNumbers(x, y)
printToConsole(x, y, result, "+")