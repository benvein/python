from os import system

name: str = None
pressedKey: str = None

print("nev: ")
name = str(input())

print("nyomjon meg egy billentyut: ")
pressedKey = str(input())

system("cls")

print(f"{name} ön a/az {pressedKey} billentyut utotte le")