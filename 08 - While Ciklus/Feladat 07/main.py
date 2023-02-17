from os import system
system("cls")

numElso: int = None
numMasik: int = None
temp: str = None
trStrElso: str = None
trStrMasik: str = None
isNumberElso: bool = False
isNumberMasik: bool = False

while (numElso == None):
    print("adjon meg egy számot: ",end="")
    temp = input()
    trStrElso = temp.replace(".", "").replace("-", "")
    isNumberElso = temp.isnumeric()

    if (isNumberElso):
        numElso = int(temp)
    else:
        print("nem számot adott meg")

while (numMasik == None or (numMasik == numElso or numMasik < numElso)):
    print(f"adjon meg egy másik számot, ami nagyobb {numElso}-nél: ",end="")
    temp = input()
    trStrMasik = temp.replace(".", "").replace("-", "")
    isNumberMasik = temp.isnumeric

    if (isNumberMasik):
        numMasik = int(temp)
    else:
        print("nem számot adott meg")

for i in range(numMasik, numElso-1, -1):
    print(i)