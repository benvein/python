from os import system

num: int = None

print("adjon meg egy szamot: ",end="")
num = int(input())

if (num>=0):
    print("pozitív")
else:
    print("a szám negatív")