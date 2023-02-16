from os import system
system("cls")

num: int = None
temp: str = None
trStr: str = None
isNumber: bool = False
osszeg: int = 0
darabszam: int = 0

while (num == None or (num < 1 or num > 99)):
    print("adjon meg egy max kétjegyű számot: ",end="")
    temp = input()
    trStr = temp.replace(".", "").replace("-", "")
    isNumber = temp.isnumeric()

    if (isNumber):
        num = int(temp)
    else:
        print("nem számot adott meg")

print("páros számok:")


for i in range(0, num, 1):
    if (i % 2 == 0):
        print(i)
    elif (i % 5 == 0):
        osszeg += i
    elif (i % 11 == 0):
        darabszam += 1

print(f"5-tel osztható számok összege: {osszeg}\n11-el osztható számok darabszáma: {darabszam}")

for j in range(0, num, 1):
    if (i % 7 == 3):
        print(f"{j}")


    



