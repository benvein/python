from os import system

name: str = None
date: int = None

print("nev: ")
name = str(input())

print("szuletesi ev: ")
date = int(input())

system("cls")

print(f"{name} ön {date}-ban/ben született")