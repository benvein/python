from typing import *
import os
from autok import Car

def readCarsFromFile(fileName: str) -> List[Car]:

    fileName: str = "data/autok.csv"
    basepath: str = os.path.dirname(os.path.abspath(__file__))
    fileFullPath: str = os.path.join(basepath, fileName)

    oneLine: str = None
    data: List[str] = []
    cars: List[Car] = []
    car: Car = None

    try:
        with open(fileFullPath, encoding="utf-8", mode="r") as file:
            for line in file:
                oneLine = line.strip()
                data = oneLine.split("\t")

                car = Car()
                car.model: data[0]
                car.mpg: float(data[1])
                car.cylinders: int(data[2])
                car.torque: float(data[3])
                car.horsepower: float(data[4])
                car.weight: int(data[5])
                car.acceleration: float(data[6])
                car.manufactureYear: int(data[7])
                car.origin: data[8]

                cars.append(car)
            
        return cars
    except FileNotFoundError as ex:
        print(f"{ex.filename} nem talalhato")
        return []