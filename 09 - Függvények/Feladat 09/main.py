from os import system
from consoleio import *
from metfunctions import *

system("cls")

jpy = "jpy"
chf = "chf"
usd = "usd"

forint: int = forintBekeres()
arfolyam: str = arfolyamBekeres(jpy, usd, chf)
konvertaltErtek: float = konvert(forint, arfolyam, jpy, usd, chf)
euro: float = euroKonvert(konvertaltErtek, arfolyam, jpy, usd, chf)

kiiratas(arfolyam, forint, jpy, usd, chf, euro)