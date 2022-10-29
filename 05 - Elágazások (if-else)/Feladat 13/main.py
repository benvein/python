from os import system

num: int = None

print("adjon meg egy számot: ",end="")
num = int(input())

if (0 < num < 9 or 10 < num < 99 or 100 < num < 999):
    if (0 < num < 9):
        print("a szám 0 és 9 között van")
    elif (10 < num < 99):
        print("a szám 10 és 99 között van")
    else:
        print("a szám 100 és 999 között van")
else:
    print("a megadott szám nem teljesíti egyik feltételt sem")