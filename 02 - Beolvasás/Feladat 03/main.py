from os import system

name: str = None
height: float = None

print("nev: ")
name = str(input())

print("magassag: ")
height = float(input())

system("cls")

print(f"{name} ön {height} meter magas")