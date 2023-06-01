from ropiIO import *
from typing import *
from ropi import Player

def writeToConsole(players: List[Player]) -> None:
    for player in players:
        print(player)