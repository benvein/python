from os import system
system("cls")

num: float = None
temp: str = None
trStr: str = None
isNumber: bool = False
osszeg: float = 0
hanyadikBevitel: int = 0

while (num == None or osszeg < 100):
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

    print(f"jelenlegi bevitel száma: {hanyadikBevitel}\njelenlegi összeg: {osszeg}")

