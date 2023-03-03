def getNumberFromConsole() -> float:
    number: float = None
    temp: str = None
    isNumber: bool = False
    truncatedString: str = None

    while (number == None):
        print("Adjon meg egy számot: ",end="")
        temp = input()
        truncatedString = temp.replace(".", "").replace("-", "")
        isNumber = truncatedString.isnumeric()

        if (isNumber):
            number = float(temp)
        else: 
            print("nem számot adott meg")   

    return number

def printToConsole(a: float, b: float, result: float, operator: str) -> None:
    print(f"{a} {operator} {b} = {result}")