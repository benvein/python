from sty import fg

def getNameFromConsole() -> str:
    name: str = None
    while (name==None or len(name)<2):
        print("adja meg a nevét: ",end="")
        name = input()

        if (len(name)<2):
            print("nem megfelelo a nev")
    
    return name.capitalize().strip()

def printToConsole(name: str) -> None:
    print(f"üdvözlöm " + fg(len(name)) + f"{name}" + fg.rs)