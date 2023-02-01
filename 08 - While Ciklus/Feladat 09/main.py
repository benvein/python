from os import system
system("cls")

print("adjon meg egy számot: ",end="")
num=int(input())

while(num / 1 < 100):
    print("háromjegyű számot adjon meg: ",end="")
    num=int(input())

if num % 7 == 0:
    print("a szám osztható 7-tel")
else:
    print("a szám nem osztható 7-tel")