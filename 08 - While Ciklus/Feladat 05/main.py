from os import system
system("cls")

hatar: float = None
num: float = None
temp: str = None
tempHatar: str = None
trStr: str = None
trStrHatar: str = None
isNumber: bool = False
isNumberHatar: bool = False
osszeg: float = 0
hanyadikBevitel: int = 0

while (hatar == None or hatar < 100):
    print("adjon meg egy határértéket 100 fölött: ",end="")
    tempHatar = input()
    trStrHatar = tempHatar.replace(".", "").replace("-", "")
    isNumberHatar = tempHatar.isnumeric()

    if (isNumberHatar):
        hatar = float(tempHatar)
    else:
        print("nem számot adott meg")

while (num == None or osszeg < hatar):
    print("adjon meg számokat: ",end="")
    temp = input()
    trStr = temp.replace(".", "").replace("-", "")
    isNumber = temp.isnumeric()

    if (isNumber):
        num = float(temp)
        osszeg += num
        hanyadikBevitel += 1
    else: 
        print("nem számot adott meg")

    print(f"jelenlegi összeg: {osszeg}")

print(f"ennyi lépésből érte el a határértéket: {hanyadikBevitel}")
