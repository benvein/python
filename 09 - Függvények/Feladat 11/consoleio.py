def nevBekeres() -> str:
    nev: str = None
    print("adjon meg egy nevet: ",end="")
    nev=input()

    return nev

def oraBekeres() -> int:
    oraszam: int = None
    temp: str = None
    trStr: str = None
    isNumeric: bool = False

    while(oraszam==None or oraszam>100 or oraszam<0):
        print("adja meg hany orat dolgozott: ",end="")
        temp=input()
        trStr = temp.replace(".", "").replace("-", "")
        isNumeric = trStr.isnumeric()

        if (isNumeric):
            oraszam = int(temp)
        else:
            ("nem szamot adott meg")

    return oraszam

def kiiratas(nev1: str, oraszam1: int, ber1: int, nev2: str, oraszam2: int, ber2: int, nev3: str, oraszam3: int, ber3: int, nev4: str, oraszam4: int, ber4: int, nev5: str, oraszam5: int, ber5: int) -> None:
    print(f"{nev1} {oraszam1} orat dolgozott, {ber1} forintot keresett\n{nev2} {oraszam2} orat dolgozott, {ber2} forintot keresett\n{nev3} {oraszam3} orat dolgozott, {ber3} forintot keresett\n{nev4} {oraszam4} orat dolgozott, {ber4} forintot keresett\n{nev5} {oraszam5} orat dolgozott, {ber5} forintot keresett")
