from os import system
from consoleio import *
from metfunctions import *

system("cls")

jpy: str = "jpy"
chf: str = "chf"
usd: str = "usd"

forint: int = forintBekeres()
arfolyam: str = arfolyamBekeres(jpy, usd, chf)
konvertaltErtek: float = konvert(forint, arfolyam)
euro: float = euroKonvert(konvertaltErtek, arfolyam)

kiiratas(arfolyam, forint, konvertaltErtek, euro)