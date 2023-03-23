def getDegreeFromConsole () -> int:
    degree: int = None
    temp: str = None
    trStr: str = None
    isNumber: bool = False
    while (degree == None):
        print("adjon meg egy hőmérsékletet Celsius fokban: ",end="")
        temp=input()
        trStr = temp.replace(".", "").replace("-", "")
        isNumber = trStr.isnumeric()

        if (isNumber):
            degree = int(temp)
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

        if (isAlpha):
            unit=str(temp)
        else: 
            print("csak betu legyen benne")

    return unit.strip().capitalize()