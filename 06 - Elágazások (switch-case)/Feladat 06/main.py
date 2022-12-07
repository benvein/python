from os import system
import math

rectangleLenght: int = None
rectangleWidth: int = None
rectangleOperations: str = None
t: int = None
k: int = None
a: float = None

print("adja meg a téglalap hosszát: ",end="")
rectangleLenght = int(input())

print("adja meg a téglalap szélességét: ",end="")
rectangleWidth = int(input())

print("adja meg a műveletet: ",end="")
rectangleOperations = str(input().lower().strip())

match rectangleOperations:
    case "t":
        t = rectangleWidth * rectangleLenght
        print(f"a téglalap területe: {t} négyzetcm")
    case "k":
        k = 2*(rectangleLenght + rectangleWidth)
        print(f"a téglalap kerülete: {k} cm")
    case "a":
        a = math.sqrt(pow(rectangleLenght, 2) + pow(rectangleWidth, 2))
        print(f"a téglalap átlója: {a} cm")
    case _:
        print("ilyen múvelet nincs")