from os import system
system("cls")

print("Pepsi [1]\nCoca Cola [2]\nSprite [3]\n Canadian dry [4]\nÁsványvíz [5]")

print("adja meg melyiket szeretné: ",end="")
valasztas=int(input())

while (valasztas<1) or (valasztas>5):
    print("nem kap üdítőt")
    break

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