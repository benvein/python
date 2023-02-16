from os import system
system("cls")

valasztas: int = None
temp: str = None
trStr: str = None
isNumber: bool = False

print("Pepsi [1]\nCoca Cola [2]\nSprite [3]\n Canadian dry [4]\nÁsványvíz [5]")

while (valasztas == None):
    print("adja meg melyik üdítőt szeretné: ",end="")
    temp = input()
    trStr = temp.replace(".", "").replace("-", "")
    isNumber = temp.isnumeric()

    if (isNumber):
        valasztas = int(temp)
        if (valasztas < 1 or valasztas > 5):
            print("nem kap üdítőt")
            break
    else:
        print("nem számot adott meg")

if valasztas==1:
    print("pepsi")
elif valasztas==2:
    print("Coca Cola")
elif valasztas==3:
    print("Sprite")
elif valasztas==4:
    print("canadian dry")
elif valasztas==5:
    print("ásványvíz")