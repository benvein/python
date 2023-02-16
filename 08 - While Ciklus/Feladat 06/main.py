from os import system
system("cls")

eletkor: int = None
temp: str = None
trStr: str = None
isNumber: bool = False

while (eletkor == None or (eletkor < 1 or eletkor > 99)):
    print("adjon meg egy érvényes életkort: ",end="")
    temp = input()
    trStr = temp.replace(".", "").replace("-", "")
    isNumber = temp.isnumeric()

    if (isNumber):
        eletkor = int(temp)
    else:
        print("nem számot adott meg")

if (eletkor > 0 and eletkor < 7):
    print("gyerek")
elif (eletkor > 6 and eletkor < 19):
    print("iskolás")
elif (eletkor > 18 and eletkor < 66):
    print("dolgozó")
else:
    print("nyugdíjas")