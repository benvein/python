def getNameFromConsole() -> str:
    name: str = None
    while (name==None or len(name)<2):
        print("adja meg a nevét: ",end="")
        name = input()

        if (len(name)<2):
            print("nem megfelelo a nev")
    
    return name.capitalize().strip()

def getYearFromConsole() -> int:
    year: int = None
    temp: str = None
    isNumber: bool = False
    truncatedString: str = None

    while (year == None or year>2023):
        print("adja meg mikor született")
        temp = input()
        truncatedString = temp.replace(".", "").replace("-", "")
        isNumber = truncatedString.isnumeric()

        if (isNumber):
            year = int(temp)
        else: 
            print("nem számot adott meg")   

    return year


def printToConsole(eletkor: int, name: str) -> None:
    print(f"{name} ön az idén {eletkor} éves")