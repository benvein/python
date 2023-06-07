from ropiIO import *
from typing import *
from ropi import Player
from ropi2 import *

def writeToConsole(players: List[Player]) -> None:
    for player in players:
        print(player)

def positionUto(players: List[Player], position: str) -> List[Player]:
    utoPosition: List[Player] = []

    for player in players:
        if(player.post == position):
            utoPosition.append(player)

    return utoPosition

def sortPlayersByAscendingHeight(players: List[Player]) -> None:
    playersCount: int = len(players)
    temp: Player = None

    for i in range(0, playersCount+1, 1):
        for j in range(i+1, playersCount):
            if (players[j].height < players[i].height):
                temp = players[i]
                players[i] = players[j]
                players[j]  = temp

def getNationalityFromFile(players: List[Player]) -> List[Nationality]:
    nationalityList: List[Nationality] = []
    player: Nationality = None

    nemzetisegek = set({})
    count: int = 0

    for player in players:
        nemzetisegek.add(player.nationality)

    for nemzetiseg in nemzetisegek:
        player = Nationality()
        player.nations = countNationality(nemzetiseg, players)
        player.countries = nemzetiseg

        nationalityList.append(player)

    return nationalityList

def countNationality(nemzetiseg: str, players: List[Player]) -> int:
    counter: int = 0
    for player in players:
        if(player.nationality==nemzetiseg):
            counter +=1

    return counter

def calculateAvgHeight(players: List[Player]) -> float:
    averageHeight: float = 0
    playerCount: int = len(players)
    totalHeight: int = 0
    
    for player in players:
        totalHeight += player.height

    averageHeight = totalHeight/playerCount

    return round(averageHeight)

def higherThanAvgPlayers(players: List[Player]) -> List[Player]:
    magasabbAtlagnal: List[Player] = []
    atlagmagassag: int = calculateAvgHeight(players)

    for player in players:
        if(player.height >= atlagmagassag):
            magasabbAtlagnal.append(player)

    return magasabbAtlagnal

    
    
