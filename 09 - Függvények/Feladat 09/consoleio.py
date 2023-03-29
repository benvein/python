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
    jpy = "jpy"
    usd = "usd"
    chf = "chf"

    while(arfolyam == None or (arfolyam != jpy or arfolyam != usd or arfolyam != chf)):
        print("adja meg melyik arfolyamba szeretne konvertalni [jpy, usd, chf]: ")
        arfolyam = input()

    return arfolyam

def kiiratas(arfolyam: str, forint: int, jpy: float, usd: float, chf: float, euro: float) -> None:
    if (arfolyam == jpy):
        print(f"{forint} forint = {jpy}¥ ami {euro}€")
    elif (arfolyam == usd):
        print(f"{forint} forint = {usd}$ ami {euro}€")
    elif (arfolyam == chf):
        print(f"{forint} forint = {chf} CHF ami {euro}€")