from ropiIO import *
from typing import *
from ropi import Player

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