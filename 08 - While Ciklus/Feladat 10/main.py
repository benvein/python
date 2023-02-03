from os import system
system("cls")

num: int = 0

while (num<1) or (num>99):
    print("max kétjegyű páros számot adjon meg: ",end="")
    num=int(input())

osszeg: int = 0
darabszam: int = 0

for i in range(0, num, 1):
    if i % 2 == 0:
        print("páros számok: ",end="")
        print(i)
    elif i % 5 == 0:
        osszeg+=i
    elif i % 11 == 0:
        darabszam+=1

print(f"öttel osztható számok összege: {osszeg}")
print(f"11-gyel oszható számok darabszáma: {darabszam}")

for j in range(0, num, 1):
    if j % 7 == 3:
        print(j)
    



