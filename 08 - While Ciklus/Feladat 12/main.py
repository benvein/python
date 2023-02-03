from os import system
system("cls")

honap: int = 0

print("mennyi megtakarított pénze van: ",end="")
penz=int(input())

while (penz>100000):
    print("már elérte a 100 000 Forintot")
    break

while (penz<100000):
    penz += (penz*0.02)
    honap += 1

print(f"{honap} hónap alatt fogja elérni a 100 000 magyar Forintot")