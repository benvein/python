from os import system

num1: int = None
num2: int = None
num3: int = None
eredmeny: float = None

print("adjon meg egy szamot: ",end="")
num1 = int(input())

print("meg egyet: ",end="")
num2 = int(input())

print("es meg egyet: ",end="")
num3 = int(input())

eredmeny = num1 * num2 / num3

print(f"eredmeny: {eredmeny}")