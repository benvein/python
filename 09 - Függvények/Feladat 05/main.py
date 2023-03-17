from os import system
from consoleio import *
from metfunctions import *

system("cls")

text1: str = getTextFromConsole()
text2: str = getSecondTextFromConsole()

sameLetter: int = countSameLetters(text1, text2)
printToConsole(sameLetter)