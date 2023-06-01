from typing import *
from ropi import Player
from ropiIO import *
from services import *

fileName: str = "data/adatok.txt"
players: List[Player] = readBooksFromFile(fileName)

writeToConsole(players)
