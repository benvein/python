from os import system
from consoleio import *
from metfunctions import *

system("cls")

hofok: float = getDegreeFromConsole()
mertekegyseg: str = getUnitFromConsole()
konvertaltHofok: float = convertToKelvin(mertekegyseg, hofok)

printToConsole(mertekegyseg, konvertaltHofok)