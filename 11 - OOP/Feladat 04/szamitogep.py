class Szamitogep:
    def __init__(self):
        super().__init__()
        self.processzor = self.Processzor()
        self.videokartya = self.Videokartya()

    class Processzor:
        def __init__(self, gyarto: str, modell: str, magok: int):
            super().__init__()
            self.gyarto: str = gyarto
            self.modell: str = modell
            self.magok: int = magok

        def __str__(self):
            return f"processzor gyártója: {self.gyarto}, modell: {self.modell}, magok száma: {self.magok}"

    class Videokartya:
        def __init__(self, gyarto: str, modell: str, vram: int):
            super().__init__()
            self.gyarto: str = gyarto
            self.modell: str = modell
            self.vram: int = vram
        
        def __str__(self):
            return f"videókártya gyártója: {self.gyarto}, modell: {self.modell}, vram: {self.vram} gb"

    class Hattertar:
        def __init__(self, gyarto: str, modell: str, meret: int, csatlakozas: str):
            super().__init__()
            self.gyarto: str = gyarto
            self.modell: str = modell
            self.meret: int = meret
            self.csatlakozas: str = csatlakozas

        def __str__(self):
            return f"Háttértár gyártója: {self.gyarto}, modell: {self.modell}, meret: {self.meret}, csatlakozás: {self.csatlakozas}"

    class Alaplap: 
        def __init__(self, gyarto: str, modell: str, tipus: str, processzorFoglalat: str):
            super().__init__()
            self.gyarto: str = gyarto
            self.modell: str = modell
            self.tipus: str = tipus
            self.processzorFoglalat: str = processzorFoglalat

        def __str__(self):
            return f"Alaplap gyartoja: {self.gyarto}, modell: {self.modell}, típus: {self.tipus}, processzorfoglalat: {self.processzorFoglalat}"

    class Tapegyseg:
        def __init__(self, gyarto: str, modell: str, teljesitmeny: int):
            super().__init__()
            self.gyarto: str = gyarto
            self.modell: str = modell
            self.teljesitmeny: int = teljesitmeny

    class RAM: 
        def __init__(self, ):
            super().__init__()

    

            
    