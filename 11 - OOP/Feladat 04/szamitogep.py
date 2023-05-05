
class Processzor:
    def __init__(self, gyarto: str, modell: str, magok: int):
        super().__init__()
        self.gyarto: str = gyarto
        self.modell: str = modell
        self.magok: int = magok

    def __str__(self):
        return f"processzor: {self.gyarto} {self.modell} {self.magok} mag"

class Videokartya:
    def __init__(self, gyarto: str, modell: str, vram: int):
        super().__init__()
        self.gyarto: str = gyarto
        self.modell: str = modell
        self.vram: int = vram
    
    def __str__(self):
        return f"videókártya: {self.gyarto} {self.modell} {self.vram} GB"

class Hattertar:
    def __init__(self, gyarto: str, modell: str, meret: int, csatlakozas: str):
        super().__init__()
        self.gyarto: str = gyarto
        self.modell: str = modell
        self.meret: int = meret
        self.csatlakozas: str = csatlakozas

    def __str__(self):
        return f"Háttértár: {self.gyarto} {self.modell} {self.meret} GB {self.csatlakozas}"

class Alaplap: 
    def __init__(self, gyarto: str, modell: str, tipus: str, processzorFoglalat: str):
        super().__init__()
        self.gyarto: str = gyarto
        self.modell: str = modell
        self.tipus: str = tipus
        self.processzorFoglalat: str = processzorFoglalat

    def __str__(self):
        return f"Alaplap: {self.gyarto} {self.modell} {self.tipus} {self.processzorFoglalat}"

class Tapegyseg:
    def __init__(self, gyarto: str, modell: str, teljesitmeny: int):
        super().__init__()
        self.gyarto: str = gyarto
        self.modell: str = modell
        self.teljesitmeny: int = teljesitmeny

    def __str__(self):
        return f"tapegyseg: {self.gyarto} {self.modell} {self.teljesitmeny}W"

class RAM: 
    def __init__(self,  gyarto: str, modell: str, meret: int):
        super().__init__()
        self.gyarto: str = gyarto
        self.modell: str = modell
        self.meret: str = meret

    def __str__(self):
        return f"RAM: {self.gyarto} {self.modell} {self.meret} GB"
    
class Szamitogep:
    def __init__(self, processzor:Processzor, videokartya:Videokartya, hattertar:Hattertar, alaplap:Alaplap, tapegyseg:Tapegyseg, ram:RAM):
        super().__init__()
        self.processzor = processzor
        self.videokartya = videokartya
        self.hattertar = hattertar
        self.alaplap = alaplap
        self.tapegyseg = tapegyseg
        self.ram = ram

    def __str__(self):
        return f"{self.processzor}\n{self.videokartya}\n{self.hattertar}\n{self.alaplap}\n{self.tapegyseg}\n{self.ram}"

            
    