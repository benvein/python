from os import system
system("cls")

print("adja meg a nevét: ",end="")
name = str(input())

while (len(name) < 2):
    print("normális nevet adjon meg: ",end="")
    name = str(input())

print(f"üdvözlöm, {name}")