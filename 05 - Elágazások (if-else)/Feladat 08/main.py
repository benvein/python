from os import system

num: int = None

print("adjon meg egy számot: ",end="")
num = int(input())

if (num % 4 == 0 and num % 6 == 0):
    print("a szám osztható 4-gyel és 6-tal")
else: 
    print("a szám nem osztható 4gyel vagy 6tal")