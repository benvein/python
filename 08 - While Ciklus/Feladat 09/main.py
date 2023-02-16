from os import system
system("cls")

num: int = None
temp: str = None
trStr: str = None
isNumber: bool = False

while (num == None or (num < 100 or num > 999)):
    print("adjon meg egy háromjegyű számot: ",end="")
    temp = input()
    trStr = temp.replace(".", "").replace("-", "")
    isNumber = temp.isnumeric()

    if (isNumber):
        num = int(temp)
    else: 
        print("nem számot adott meg")

if (num % 7 == 0):
    print("a szám osztható 7-tel")
else:
    print("nem oszható 7-tel a szám")
    