from os import system

name: str = None

print("adja meg a nevét: ",end="")
name = str(input())

while (len(name) < 2):
    print("normális nevet adjon meg: ",end="")
    name = str(input())

print(f"üdvözlöm, {name}")