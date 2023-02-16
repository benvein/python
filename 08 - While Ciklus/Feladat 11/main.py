from os import system
import random
system("cls")

numParatlan: int = None
numParos: int = None

tempParos: str = None
tempParatlan: str = None
trStrParos: str = None
trStrParatlan: str = None
isNumberParos: bool = False
isNumberParatlan: bool = False 

osszeg: int = 0
darabszam: int = 0
darabszamNegy: int = 0

while (numParos == None) or (numParos % 2 != 0):
    print("egy páros számot adjon meg: ",end="")
    tempParos = input()
    trStrParos = tempParos.replace(".", "").replace("-", "")
    isNumberParos = tempParos.isnumeric()

    if (isNumberParos):
        numParos = int(tempParos)
    else:
        print("nem számot adott meg")

while (numParatlan == None or ((numParatlan<numParos) or (numParatlan % 2 == 0))):
    print("az előzőnél egy nagyobb páratlan számot adjon meg: ",end="")
    tempParatlan = input()
    trStrParatlan = tempParatlan.replace(".", "").replace("-", "")
    isNumberParatlan = tempParatlan.isnumeric()

    if (isNumberParatlan):
        numParatlan = int(tempParatlan)
    else:
        print("nem számot adott meg")

randomNum = random.randint(numParos, numParatlan)

print(f"a random szám {randomNum}")

if (randomNum-numParos) > (numParatlan-randomNum):
    print("a páros szám van messzebb a random számtól")
else:
    print("a páratlan szám van messzebb a random számtól")

for i in range(numParos, numParatlan, 1):
    osszeg += i
    darabszam += 1
    if i % 4 == 0:
        darabszamNegy += 1

atlag = osszeg/darabszam

print(f"a 2 szám közti számok átlaga: {atlag}")
print(f"a 4-gyel oszható számok darabszáma: {darabszamNegy}")

