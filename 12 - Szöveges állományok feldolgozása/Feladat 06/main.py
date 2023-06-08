from typing import *
from services import *
from autoIO import *
from autok import Car
import os

fileName: str = "data/autok.csv"
cars: List[Car] = readCarsFromFile(fileName)

carCounter: int = howManyCars(cars)
print(f"Az autok.csv allomanyban {carCounter} auto szerepel")

sumWeight: int = sumOfWeight(cars)
print(f"Az autok.csv allomanyban szereplo autok ossz sulya {sumWeight}kg")

biggestTorque: float = carWithBiggestTorque(cars)
print(f"A legnagyobb nyomatékkal a rendelkezik ({biggestTorque}Nm)")