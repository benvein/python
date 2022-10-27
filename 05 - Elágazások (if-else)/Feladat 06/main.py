from os import system

num1: int = None
num2: int = None
num3: int = None

print("szam1: ",end="")
num1 = int(input())

print("szam 2: ",end="")
num2 = int(input())

print("szam 3: ",end="")
num3 = int(input())

if (num1 > num2 and num2 > num3):
    print(f"a számok sorrendben: {num3}, {num2}, {num1}")
elif (num1 > num2 and num3 > num2):
    print(f"a számok sorrendben: {num2}, {num3}, {num1}")
elif (num2 > num1 and num1 > num3):
    print(f"a számok sorrendben: {num3}, {num1}, {num2}")
elif (num2 > num1 and num3 > num1):
    print(f"a számok sorrendben: {num1}, {num3}, {num2}")
elif (num3 > num1 and num1 > num2):
    print(f"a számok sorrendben: {num2}, {num1}, {num3}")
elif (num3 > num1 and num2 > num1):
    print(f"a számok sorrendben: {num1}, {num2}, {num3}")