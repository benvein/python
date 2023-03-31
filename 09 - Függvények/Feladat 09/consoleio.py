def forintBekeres() -> int:
    forint: int = None
    temp: str = None
    trStr: str = None
    isNumber: bool = False

    while(forint == None):
        print("adja meg mennyi forintot szeretne atkovertalni: ",end="")
        temp = input()
        trStr = temp.replace(".", "").replace("-", "")
        isNumber = trStr.isnumeric()

        if (isNumber):
            forint = int(temp)
        else: 
            print("nem szamot adott meg")

    return forint

def arfolyamBekeres(jpy: str, usd: str, chf: str) -> str:
    arfolyam: str = None

    while(arfolyam == None or (arfolyam != "jpy" or arfolyam != "usd" or arfolyam != "chf")):
        print("adja meg melyik arfolyamba szeretne konvertalni [jpy, usd, chf]: ")
        arfolyam = input()

    if (arfolyam == "jpy"):
        arfolyam = str(jpy)
    elif (arfolyam == "usd"):
        arfolyam = str(usd)
    elif (arfolyam == "chf"):
        arfolyam = str(chf)

    return arfolyam

def kiiratas(arfolyam: str, forint: int, konvertaltErtek: float, euro: str) -> None:
    if (arfolyam == "jpy"):
        print(f"{forint} forint = {konvertaltErtek}¥ ami {euro}€")
    elif (arfolyam == "usd"):
        print(f"{forint} forint = {konvertaltErtek}$ ami {euro}€")
    elif (arfolyam == "chf"):
        print(f"{forint} forint = {konvertaltErtek} CHF ami {euro}€")