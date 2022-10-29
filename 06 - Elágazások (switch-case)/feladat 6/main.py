from os import system
import math

rectangleLenght: int = None
rectangleWidth: int = None
rectangleOperations: str = ["t", "k", "a"]

print("adja meg a téglalap hosszát: ",end="")
rectangleLenght = int(input())

print("adja meg a téglalap szélességét: ",end="")
rectangleWidth = int(input())

print("adja meg a műveletet: ",end="")
rectangleOperations = str(input())

t = rectangleWidth * rectangleLenght
k = 2*(rectangleLenght + rectangleWidth)
a = float(math.sqrt(pow(rectangleLenght, 2) + pow(rectangleWidth, 2)))

match rectangleOperations:
    case "t":
        print(f"a téglalap területe: {t} négyzetcm")
    case "k":
        print(f"a téglalap kerülete: {k} cm")
    case "a":
        print(f"a téglalap átlója: {a} cm")