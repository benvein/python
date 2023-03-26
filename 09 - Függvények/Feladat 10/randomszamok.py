import random

def elsoRandom() -> int:
    rndEgy: int = random.randint(0,9)
    return rndEgy

def masodikRandom() -> int:
    rndKetto: int = random.randint(40, 50)
    return rndKetto

def harmadikRandom(rndEgy: int, rndKetto: int) -> int:
    rndHarom: int = random.randint(rndEgy, rndKetto)
    return rndHarom