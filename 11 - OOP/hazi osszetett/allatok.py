from medve import *
from pingvin import *
from oroszlan import *
from elefant import *
from zebra import *
from tigris import *

class Allatok:
    def __init__(self, medve: Medve, pingvin: Pingvin, oroszlan: Oroszlan, elefant: Elefant, zebra: Zebra, tigris: Tigris):
        super().__init__()
        self.medve = medve
        self.pingvin = pingvin
        self.oroszlan = oroszlan
        self.elefant = elefant
        self.zebra = zebra
        self.tigris = tigris

    def __str__(self):
        return f"Állatkert legnépszerűbb tagjai\n{self.medve}\n{self.pingvin}\n{self.oroszlan}\n{self.elefant}\n{self.zebra}\n{self.tigris}"