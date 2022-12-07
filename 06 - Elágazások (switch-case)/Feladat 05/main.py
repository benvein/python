from os import system

resistance1: int = None
resistance2: int = None
seriesConn: int = None
parallelConn: float = None
connType: str = None
result: float = None

print("adja meg az első ellenállás értékét: ",end="")
resistance1 = int(input())

print("adja meg a második ellenállás értékét: ",end="")
resistance2 = int(input())

print("adja meg a kapcsolás típusát (s vagy p): ",end="")
connType = str(input().lower().strip())

match connType:
    case "s":
        result = resistance1 + resistance2
        print(f"az ellenállások eredő értéke soros kapcsolás esetén: {result}Ω")
    case "p":
        result = (resistance1 + resistance2) / (resistance1 * resistance2)
        print(f"az ellenállások eredő értéke párhuzamos kapcsolás esetén: {result}Ω")
    case _:
        print("ilyen kapcsolás nincs")