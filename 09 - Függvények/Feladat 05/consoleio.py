def getTextFromConsole() -> str:
    text1: str = None
    temp: str = None
    isAlpha: bool = False
    while(text1==None):
        print("adjon meg egy szót: ",end="")
        temp=input()
        isAlpha=temp.isalpha()

        if (isAlpha):
            text1=str(temp)
        else: 
            print("csak betu legyen benne")

def getSecondTextFromConsole() -> str:
    text2: str = None
    temp: str = None
    isAlpha: bool = False
    while(text2==None):
        print("adjon meg még egy szót: ",end="")
        temp=input()
        isAlpha=temp.isalpha()

        if (isAlpha):
            text2=str(temp)
        else: 
            print("csak betu legyen benne")

def printToConsole(sameLetter: int) -> None:
    print(f"megegyező betűk száma: {sameLetter}")
