from os import system

num1: float = None
num2: float = None
num3: float = None
eredmeny: float = None

print("elso szam: ",end="")
num1 = float(input())

print("masodik szam: ",end="")
num2 = float(input())

print("harmadik szam: ",end="")
num3 = float(input())

num1 = num1 + 0,5
num2 = num2 - 0,7

eredmeny = (num1 * num2) % num3

print(f"eredmeny: {eredmeny}")