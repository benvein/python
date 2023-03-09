def getTextFromConsole() -> str:
    text1: str = None
    text2: str = None
    while(text1==None):
        print("adjon meg egy szót: ",end="")
        text1 = input()
        if(text1.isalpha()==False):
            print("csak betu legyen benne")
     
    while(text2==None or text2.isalpha()==False):
        print("adjon meg még egy szót: ",end="")
        text2 = input()
        if(text2.isalpha()==False):
            print("csak betu legyen benne")

    return text1, text2

def printToConsole(sameLetter: int) -> None:
    print(f"megegyező betűk száma: {sameLetter}")
