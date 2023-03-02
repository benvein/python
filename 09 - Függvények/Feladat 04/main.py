from os import system
system("cls")
system("color A")
import sty

nev: str = None

def nevBekeres(nev: str) -> str:
    print("adja meg a nevét: ")
    nev = input()

    return nev

bekertNev: str = nevBekeres(nev)

print(f"Üdvözlöm {bekertNev}")