from os import system 
system("cls")

jelenlegiEv: int = 2023
temp: str = None
trStr: str = None
isNumber: bool = False
szulEv: int = None
nev: str = None



def szuletesiEv(szulEv: int) -> int:
    while (szulEv == None):
        print("adja meg mikor született: ")
        temp = input()
        trStr = temp.replace(".", "").replace("-", "")
        isNumber = temp.isnumeric() 

        if (isNumber):
            szulEv = int(temp)
        else:
            print("nem számot adott meg")
        
    return szulEv

def neve(nev: str) -> str:
    while (nev == None or len(nev) < 2):
        print("adja meg a nevét: ")
        nev = input()

    return nev

szuletEv: int = szuletesiEv(szulEv)
neev: str = neve(nev)

print(f"{neev} on {szuletEv}-ban szuletett")