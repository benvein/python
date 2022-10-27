from os import system

num: int = None

print("adjon meg egy számot: ",end="")
num = int(input())

if (num % 5 == 0):
    print("a szám osztható 5-tel")
else:
    print("a szám nem osztható 5-tel")