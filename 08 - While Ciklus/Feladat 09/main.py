from os import system
system("cls")

num: int = None

while (num == None) or (num / 1 < 100):
    print("háromjegyű számot adjon meg: ",end="")
    num=int(input())

if num % 7 == 0:
    print("a szám osztható 7-tel")
else:
    print("a szám nem osztható 7-tel")