from os import system
system("cls")

numElso: int = None
numMasik: int = None
tempElso: str = None
tempMasik: str = None
trStrElso: str = None
trStrMasik: str = None
isNumberElso: bool = False
isNumberMasik: bool = False

while (numElso == None):
    print("adjon meg egy számot: ",end="")
    tempElso = input()
    trStrElso = tempElso.replace(".", "").replace("-", "")
    isNumberElso = tempElso.isnumeric()

    if (isNumberElso):
        numElso = int(tempElso)
    else:
        print("nem számot adott meg")

while (numMasik == None or (numMasik == numElso or numMasik < numElso)):
    print(f"adjon meg egy másik számot, ami nagyobb {numElso}-nél: ",end="")
    tempMasik = input()
    trStrMasik = tempMasik.replace(".", "").replace("-", "")
    isNumberMasik = tempMasik.isnumeric

    if (isNumberMasik):
        numMasik = int(tempMasik)
    else:
        print("nem számot adott meg")

for i in range(numMasik, numElso-1, -1):
    print(i)