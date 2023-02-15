from os import system
system("cls")

print("adjon meg egy számot: ",end="")
szam = int(input())

osszeg = szam
proba=1

while osszeg<100: #egész újra
    print("adjon meg egy számot: ",end="")
    szam=int(input())
    proba+=1
    osszeg = osszeg + szam

print(f"ennyi próba kellett: {proba}")
print(osszeg)
