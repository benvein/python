from os import system
from consoleio import *
from metfunctions import *

system("cls")

xEgy: int = elsoX()
yEgy: int = elsoY()
xKetto: int = masodikX()
yKetto: int = masodikY()

tavolsag: float = kiszamolas(xEgy, xKetto, yEgy, yKetto)

kiiratas(xEgy, xKetto, yEgy, yKetto, tavolsag)