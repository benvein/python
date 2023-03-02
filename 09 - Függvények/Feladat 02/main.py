from os import system
system("cls")

nev: str = input("adja meg a nevét: ")

def nevFv(nev: str) -> str:
    return nev

felhasznalo: str = nevFv(nev)
print(f"üdvözlöm {nev}")