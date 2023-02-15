from os import system
system("cls")

hatar: int = 0
proba: int =1
osszeg: int = 0


while hatar<100:
    print("100 fölötti értéket adjon meg: ",end="")
    hatar=int(input()) #vizsgálat

print("számolj: ",end="")
szam=int(input())


while osszeg<100:
    print("adj még meg számot: ",end="")
    szam=int(input())
    proba+=1
    osszeg+=szam

print(f"{proba} próbálkozásból sikerült")
print(osszeg)
