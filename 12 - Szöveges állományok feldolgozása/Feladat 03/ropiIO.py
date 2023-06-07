from typing import *
import os
from ropi import Player
from io import open
from ropi2 import *

def readPlayersFromFile(fileName: str) -> List[Player]:

    fileName: str = "data/adatok.txt"
    basepath: str = os.path.dirname(os.path.abspath(__file__))
    fileFullPath: str = os.path.join(basepath, fileName)

    oneLine: str = None
    data: List[str] = []
    players: List[Player] = []
    player: Player = None

    try:
        with open(fileFullPath,encoding="utf-8", mode="r") as file:
            for line in file:
                oneLine = line.strip() 
                data = oneLine.split('\t')

                player = Player()
                player.name = data[0]
                player.height = int(data[1])
                player.post = data[2]
                player.nationality = data[3]
                player.team = data[4]
                player.country = data [5]

                players.append(player)

        return players
    except FileNotFoundError as ex:
        print(f"{ex.filename} nem talalhato")
        return []

def writePlayersToFile(players: List[Player], fileName: str) -> None:
    basepath: str = os.path.dirname(os.path.abspath(__file__))
    basepath += "/output"
    fileFullPath: str = os.path.join(basepath, fileName)

    try:
        with open(fileFullPath, encoding="utf-8", mode="w") as file:
            for player in players:
                file.write(f"{player.name}, {player.height}cm, {player.post}, {player.nationality}, {player.team}, {player.country}\n")
    except FileNotFoundError as ex:
        print(f"{ex.filename} nem talalhato")

def writePlayersToFileNationality(players: List[Nationality], fileName: str) -> None:
    basepath: str = os.path.dirname(os.path.abspath(__file__))
    basepath += "/output"
    fileFullPath: str = os.path.join(basepath, fileName)

    try:
        with open(fileFullPath, encoding="utf-8", mode="w") as file:
            for player in players:
                file.write(f"{player.countries}: {player.nations}\n")
    except FileNotFoundError as ex:
        print(f"{ex.filename} nem talalhato")