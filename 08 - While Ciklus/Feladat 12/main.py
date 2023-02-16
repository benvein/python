from os import system
system("cls")

honap: int = 0
penz: int = None
temp: str = None
trStr: str = None
isNumber: bool = False

while (penz == None or (penz>100000)):
    print("mennyi pénze van: ",end="")
    temp = input()
    trStr = temp.replace(".", "").replace("-", "")
    isNumber = temp.isnumeric()

    if (isNumber):
        penz = int(temp)
        if (penz>100000):
            print("már elérte a 100.000 Forintot")
            break
    else:
        print("nem számot adott meg")

while (penz<100000):
    penz += (penz*0.02)
    honap += 1

print(f"{honap} hónap alatt fogja elérni a 100 000 magyar Forintot")

