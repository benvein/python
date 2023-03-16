def getFirstNameFromConsole() -> str:
    name: str = None
    while (name==None or len(name)<2):
        print("adja meg az első dolgozó nevét: ",end="")
        name = input()

        if (len(name)<2):
            print("nem megfelelo a nev")
    
    return name.capitalize().strip()

def getSecondNameFromConsole() -> str:
    name: str = None
    while (name==None or len(name)<2):
        print("adja meg a második dolgozó nevét: ",end="")
        name = input()

        if (len(name)<2):
            print("nem megfelelo a nev")
    
    return name.capitalize().strip()

def getThirdNameFromConsole() -> str:
    name: str = None
    while (name==None or len(name)<2):
        print("adja meg a harmadik dolgozó nevét: ",end="")
        name = input()

        if (len(name)<2):
            print("nem megfelelo a nev")
    
    return name.capitalize().strip()

def getFourthNameFromConsole() -> str:
    name: str = None
    while (name==None or len(name)<2):
        print("adja meg a negyedik dolgozó nevét: ",end="")
        name = input()

        if (len(name)<2):
            print("nem megfelelo a nev")
    
    return name.capitalize().strip()

def getFifthNameFromConsole() -> str:
    name: str = None
    while (name==None or len(name)<2):
        print("adja meg az ötödik dolgozó nevét: ",end="")
        name = input()

        if (len(name)<2):
            print("nem megfelelo a nev")
    
    return name.capitalize().strip()

def firstPersonWorkingHour(nameOne: str) -> int:
    workinghour: int = None
    temp: str = None
    isNumber: bool = False
    truncatedString: str = None

    while (workinghour == None or workinghour<0):
        print(f"adja meg mennyit dolgozott {nameOne}")
        temp = input()
        truncatedString = temp.replace(".", "").replace("-", "")
        isNumber = truncatedString.isnumeric()

        if (isNumber):
            workinghour = int(temp)
        else: 
            print("nem számot adott meg")   

    return workinghour

def secondPersonWorkingHour(nameTwo: str) -> int:
    workinghour: int = None
    temp: str = None
    isNumber: bool = False
    truncatedString: str = None

    while (workinghour == None or workinghour<0):
        print(f"adja meg mennyit dolgozott {nameTwo}")
        temp = input()
        truncatedString = temp.replace(".", "").replace("-", "")
        isNumber = truncatedString.isnumeric()

        if (isNumber):
            workinghour = int(temp)
        else: 
            print("nem számot adott meg")   

    return workinghour

def thirdPersonWorkingHour(nameThree: str) -> int:
    workinghour: int = None
    temp: str = None
    isNumber: bool = False
    truncatedString: str = None

    while (workinghour == None or workinghour<0):
        print(f"adja meg mennyit dolgozott {nameThree}")
        temp = input()
        truncatedString = temp.replace(".", "").replace("-", "")
        isNumber = truncatedString.isnumeric()

        if (isNumber):
            workinghour = int(temp)
        else: 
            print("nem számot adott meg")   

    return workinghour

def fourthPersonWorkingHour(nameFour: str) -> int:
    workinghour: int = None
    temp: str = None
    isNumber: bool = False
    truncatedString: str = None

    while (workinghour == None or workinghour<0):
        print(f"adja meg mennyit dolgozott {nameFour}")
        temp = input()
        truncatedString = temp.replace(".", "").replace("-", "")
        isNumber = truncatedString.isnumeric()

        if (isNumber):
            workinghour = int(temp)
        else: 
            print("nem számot adott meg")   

    return workinghour

def fifthPersonWorkingHour(nameFive: str) -> int:
    workinghour: int = None
    temp: str = None
    isNumber: bool = False
    truncatedString: str = None

    while (workinghour == None or workinghour<0):
        print(f"adja meg mennyit dolgozott {nameFive}")
        temp = input()
        truncatedString = temp.replace(".", "").replace("-", "")
        isNumber = truncatedString.isnumeric()

        if (isNumber):
            workinghour = int(temp)
        else: 
            print("nem számot adott meg")   

    return workinghour

def printToConsole(nameOne: str, nameTwo: str, nameThree: str, nameFour: str, nameFive: str, workinghourOne: int, workingourTwo: int, workinghourThree: int, workinghourFour: int, workinghourFive: int) -> None:
    print("")