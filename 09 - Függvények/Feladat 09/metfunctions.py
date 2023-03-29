def konvert(forint: int, arfolyam: str) -> float:
    konvertaltErtek: float = None
    if (arfolyam == "jpy"):
        konvertaltErtek = forint * 0.37
    elif (arfolyam == "usd"):
        konvertaltErtek = forint * 0.0028
    elif (arfolyam == "chf"):
        konvertaltErtek = forint * 0.0026

    return konvertaltErtek

def euroKonvert(konvertaltErtek: float, arfolyam: str) -> float: 
    euro: float = None
    if(arfolyam=="jpy"):
        euro = konvertaltErtek * 0.75
    elif(arfolyam=="usd"):
        euro = konvertaltErtek * 0.8
    elif(arfolyam=="chf"):
        euro = konvertaltErtek * 0.55
    
    return euro