from os import system
system("cls")

name: str = None

while (name == None) or (len(name) < 2):
    print("normális nevet adjon meg: ",end="")
    name = str(input())

print(f"üdvözlöm, {name}")