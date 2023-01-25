from os import system
system("cls")

num: float = None
temp: str = None
isNumber: bool = False
truncatedString: str = None

while (num == None or (num < 0 or num > 9)):
    print("Adjon meg egy számot: ",end="")
    temp = input()
    truncatedString = temp.replace(".", "").replace("-", "")
    isNumber = truncatedString.isnumeric()

    if (isNumber):
        num = float(temp)
    else: 
        print("nem számot adott meg")