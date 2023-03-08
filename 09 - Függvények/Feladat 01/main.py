from os import system
system("cls")
from metfunctions import *
from consoleio import *

x: float = None
y: float = None
result: float = None
resultDiv: float = None
resultMul: float = None
resultSub: float = None

x = getNumberFromConsole()
y = getNumberFromConsole()

result = sumOfTwoNumbers(x, y)
resultDiv = divide(x, y)
resultMul = multiple(x, y)
resultSub = substraction(x, y)

printToConsole(x, y, result, "+")
printToConsole(x, y, resultDiv, "/")
printToConsole(x, y, resultMul, "*")
printToConsole(x, y, resultSub, "-")

