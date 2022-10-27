from os import system

num1: int = None
num2: int = None

print("adjon meg egy egesz szamot: ",end="")
num1 = int(input())

print("adjoj meg meg egyet: ",end="")
num2 = int(input())

if (num1 > num2):
    print(f"sorrendben a két szám: {num2}, {num1}")
else:
    print(f"sorrendben a két szám: {num1}, {num2}")