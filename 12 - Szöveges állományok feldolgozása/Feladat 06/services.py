from typing import *
from autoIO import *
from autok import Car

def howManyCars(cars: List[Car]) -> int:
    carCounter: int = 0

    for car in cars:
        carCounter += 1

    return carCounter

def sumOfWeight(cars: List[Car]) -> int:
    sumWeight: int = 0

    for car in cars:
        sumWeight += car.weight

    return sumWeight

def carWithBiggestTorque(cars: List[Car]) -> Car:
    biggestTorque: Car = cars[0]

    for index in range(1, len(cars), 1):
        if(cars[index].torque > biggestTorque.torque):
            biggestTorque = cars[index]

    return biggestTorque