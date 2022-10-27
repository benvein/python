from os import system

szam1: int = None
szam2: int = None
eredmeny: int = None

print("adjon meg egy szamot: ",end="")
szam1 = int(input())

print ("adjon meg meg egy szamot: ",end="")
szam2 = int(input())

eredmeny = szam1 + szam2

print(f"eredmeny: {eredmeny}")