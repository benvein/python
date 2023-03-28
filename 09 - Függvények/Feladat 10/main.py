from os import system
from consoleio import *
from randomszamok import *
from szamlalo import *

system("cls")

rndEgy: int = elsoRandom()
rndKetto: int = masodikRandom()
rndHarom: int = harmadikRandom(rndEgy, rndKetto)
tipp: int = tippBekeres(rndEgy, rndKetto, rndHarom)
tippSzamlalo: int = tippSzamolas(tipp, rndHarom)

kiiratas(tippSzamlalo)