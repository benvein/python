from os import system
system("cls")

from consoleio import *
from metfunctions import *

sameLetter: int = None
text1: str = None
text2: str = None

text1 = getTextFromConsole()
text2 = getTextFromConsole()

sameLetter = check(text1, text2)
printToConsole(sameLetter)