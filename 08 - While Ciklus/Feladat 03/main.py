from os import system
import random
system("cls")

randomNum = random.randint(0, 9)
num: float = None
probalkozas: int = 0
temp: str = None
trStr: str = None
isNumber: bool = False


while (num == None) or ((num != randomNum) and (probalkozas < 5)): 
    print("adjon meg egy 0 és 9 közötti számot: ",end="")
    temp = input()
    trStr = temp.replace(".", "").replace("-", "")
    isNumber = trStr.isnumeric()

    if (isNumber):
        num = float(temp)
        probalkozas += 1
        if (probalkozas == 5):
            print("nem találtad ki")
            break
    else: 
        print("nem számot adott meg")

