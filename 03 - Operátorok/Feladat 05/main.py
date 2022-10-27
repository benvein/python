from os import system

num1: int = None
num2: int = None
num3: int = None
num4: int = None
eredmeny: float = None

print("elso szam: ",end="")
num1 = int(input())

print("masodik szam: ",end="")
num2 = int(input())

print("harmadik szam: ",end="")
num3 = int(input())

print("negyedik szam: ",end="")
num4 = int(input())

eredmeny = (num1 + num2) / (num3 - num4)

print(f"eredmeny: {eredmeny}")