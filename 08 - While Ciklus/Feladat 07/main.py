from os import system
system("cls")

print("adjon meg egy szamot: ",end="")
num=int(input())

print("meg egyet: ",end="")
numMasik=int(input())

while (num == numMasik):
    print("masik szamot adjon meg: ",end="")
    numMasik=int(input())

if (num>numMasik):
    for i in range(num, numMasik-1, -1):
        print(i)
else:
    for i in range(numMasik, num-1, -1):
        print(i)
