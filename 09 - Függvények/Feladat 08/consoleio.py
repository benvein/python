def elsoX() -> int:
    xEgy: int = None
    temp: str = None
    isNumber: bool = False
    truncatedString: str = None

    while (xEgy == None):
        print("adja meg az elso pont X erteket: ",end="")
        temp = input()
        truncatedString = temp.replace(".", "").replace("-", "")
        isNumber = truncatedString.isnumeric()

        if (isNumber):
            xEgy = int(temp)
        else: 
            print("nem számot adott meg")   

    return xEgy

def elsoY() -> int:
    yEgy: int = None
    temp: str = None
    isNumber: bool = False
    truncatedString: str = None

    while (yEgy == None):
        print("adja meg az elso pont Y erteket: ",end="")
        temp = input()
        truncatedString = temp.replace(".", "").replace("-", "")
        isNumber = truncatedString.isnumeric()

        if (isNumber):
            yEgy = int(temp)
        else: 
            print("nem számot adott meg")   

    return yEgy

def masodikX() -> int:
    xKetto: int = None
    temp: str = None
    isNumber: bool = False
    truncatedString: str = None

    while (xKetto == None):
        print("adja meg a masodik pont X erteket: ",end="")
        temp = input()
        truncatedString = temp.replace(".", "").replace("-", "")
        isNumber = truncatedString.isnumeric()

        if (isNumber):
            xKetto = int(temp)
        else: 
            print("nem számot adott meg")   

    return xKetto

def masodikY() -> int:
    yKetto: int = None
    temp: str = None
    isNumber: bool = False
    truncatedString: str = None

    while (yKetto == None):
        print("adja meg a masodik pont Y erteket: ",end="")
        temp = input()
        truncatedString = temp.replace(".", "").replace("-", "")
        isNumber = truncatedString.isnumeric()

        if (isNumber):
            yKetto = int(temp)
        else: 
            print("nem számot adott meg")   

    return yKetto

def kiiratas(xEgy: int, xKetto: int, yEgy: int, yKetto: int, tavolsag: float) -> None:
    print(f"A ({xEgy}, {yEgy}) es ({xKetto}, {yKetto}) pontok tavolsaga: {tavolsag}")