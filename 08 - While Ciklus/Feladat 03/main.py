from os import system
import random
system("cls")

randomNum = random.randint(0, 9)
num: int = None
probalkozas: int = 0

print("0 és 9 közötti szám: ",end="")
num = int(input())

#print(randomNum)

while num != randomNum:
    print("nem talált")
    num=int(input())
    probalkozas += 1
    if probalkozas == 4:
        print("L")
        break

if randomNum == num:
    print("W")