from typing import *
from ropi import Player
from ropiIO import *
from services import *
from ropi2 import *

fileName: str = "data/adatok.txt"
players: List[Player] = readPlayersFromFile(fileName)

writeToConsole(players)


#Keressük ki az ütő játékosokat az utok.txt állömányba
utoPosition: List[Player] = positionUto(players, "ütő")
writePlayersToFile(utoPosition, "utok.txt")

#Rendezzük a játékosokat magasság szerint növekvő sorrendbe és a magaslatok.txt állományba mentsük el.
sortPlayersByAscendingHeight(players)
writePlayersToFile(players, "magaslatok.txt")

#- Mutassuk be a nemzetisegek.txt állományba, hogy mely nemzetiségek képviseltetik magukat a röplabdavilágban mint játékosok és milyen számban. (uj osztaly, set)
naciok: List[Nationality] = getNationalityFromFile(players)
writePlayersToFileNationality(naciok, "nemzetisegek.txt")

#atlagnalmagasabbak.txt állományba keressük azon játékosok nevét és magasságát akik magasabbak mint az „adatbázisban” szereplő játékosok átlagos magasságánál.
magasabbAtlagnal: List[Player] = higherThanAvgPlayers(players)
writePlayersToFile(players, "atlagnalmagasabb.txt")

