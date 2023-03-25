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