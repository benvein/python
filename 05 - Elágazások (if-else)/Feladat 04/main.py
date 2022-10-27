from os import system

num1: int = None
num2: int = None

print("adjon meg egy szamot: ",end="")
num1 = int(input())

print("még egyet: ",end="")
num2 = int(input())

if (num1 > num2):
    print(f"{num1} a nagyobb")
else: 
    print(f"{num2} a nagyobb")