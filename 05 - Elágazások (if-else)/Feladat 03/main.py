from os import system

num: int = None

print("adjon meg egy számot: ",end="")
num = int(input())

if (num > -30 and num < 40):
    print=("a szám -30 és 40 között van")
else: 
    print("a szám kisebb mint -30 vagy nagyobb mint 40")