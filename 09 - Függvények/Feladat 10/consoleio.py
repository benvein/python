def tippBekeres(rndEgy: int, rndKetto: int, rndHarom: int) -> int:
    tipp: int = None
    temp: str = None
    trStr: str = None
    isNumber: bool = False

    while (tipp==None or tipp>rndKetto or tipp<rndEgy):
        print(f"adja meg a tippjet {rndEgy} es {rndKetto} kozott: ",end="")
        temp = input()
        trStr = temp.replace("-", "").replace(".", "")
        isNumber = trStr.isnumeric()

        if(isNumber):
            tipp = int(temp)
            if (tipp > rndHarom):
                print("kisebb a kitalalando szam")
            elif(tipp<rndHarom):
                print("nagyobb a kitalalando szam")
        else:
            print("nem szamot adott meg")

    return tipp

def tippSzamolas(tipp: int, rndHarom: int, rndEgy: int, rndKetto: int) -> int:
    tippSzamlalo: int = 1
    while (tipp != rndHarom):
        tipp = tippBekeres(rndEgy, rndKetto, rndHarom)
        tippSzamlalo += 1

    return tippSzamlalo

def kiiratas(tippSzamlalo: int) -> None:
    print(f"ennyi probalkozasbol sikerult kitalalni: {tippSzamlalo}")