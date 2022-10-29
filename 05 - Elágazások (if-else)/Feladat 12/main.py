from os import system

num: int = None

print("adjon meg egy szamot: ",end="")
num = int(input())

if (10 < num < 20 or -20 < num < -10):
    if (10 < num < 20):
        print("a szám 10 és 20 között van")
    else:
        print("a szám -20 és -10 között van")
else:
    print("a szám sem 10 és 20 között, és sem -20 és -10 közt nincs")