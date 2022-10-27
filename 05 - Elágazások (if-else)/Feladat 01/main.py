from os import system

num: int = None

print("adjon meg egy szamot: ",end="")
num = int(input())

if (num>0):
    print("a szám nagyobb 0-nál")
else:
    print("a szám kisebb 0-nál")