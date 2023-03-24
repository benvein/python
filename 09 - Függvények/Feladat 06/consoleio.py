def getDegreeFromConsole () -> float:
    degree: float = None
    temp: str = None
    trStr: str = None
    isNumber: bool = False
    while (degree == None):
        print("adjon meg egy hőmérsékletet Celsius fokban: ",end="")
        temp=input()
        trStr = temp.replace(".", "").replace("-", "")
        isNumber = trStr.isnumeric()

        if (isNumber):
            degree = float(temp)
        else:
            print("nem szamot adott meg")

    return degree

def getUnitFromConsole () -> str:
    unit: str = None
    temp: str = None
    isAlpha: bool = False
    while(unit==None):
        print("adja meg a mertekegyseget(Kelvin vagy Fahrenheit): ",end="")
        temp=input()
        isAlpha=temp.isalpha()

        if (isAlpha and (temp=="K" or temp=="Kelvin" or temp=="F" or temp=="Farenheit")):
            unit=str(temp)
        else: 
            print("csak betu legyen benne")

    return unit.strip().capitalize()

def printToConsole(mertekegyseg: str, konvertaltHofok: int) -> None:
    print(f"az atalakitott hofok: {konvertaltHofok} {mertekegyseg}")