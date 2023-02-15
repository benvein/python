from os import system
import random
system("cls")

randomNum = random.randint(0, 9)
num: int = None
probalkozas: int = 0
num: int = None

#print(randomNum)

while (num == None) or ((num != randomNum) and (probalkozas < 5)): #nem jó feltétel még nem találta el és van próbálkozási lehetősége
    print("adjon meg egy 0 és 9 közötti számot: ",end="")