import math

def kiszamolas(xEgy: int, xKetto: int, yEgy: int, yKetto: int) -> float:
    tavolsag: float = None
    tavolsag = math.sqrt(math.pow(xKetto - xEgy, 2) + math.pow(yKetto - yEgy, 2))

    return round(tavolsag, 2)