class Szamitogep:
    def __init__(self):
        super().__init__()
        self.processzor = self.Processzor("Intel", "Pentium", 4)
        self.videokartya = self.Videokartya("Nvidia", "GT910", 1)
        self.hattertar = self.Hattertar("Kingston", "W1000", 1000, "SATA6")
        self.alaplap = self.Alaplap("Asus", "ROG strix", "ATX", "Intel 9th gen")
        self.tapegyseg = self.Tapegyseg("NZXT", "idk", 1000)
        self.ram = self.RAM("Kingston", "eztsetudom", 8)

    def __str__(self):
        return f"{self.processzor}\n{self.videokartya}\n{self.hattertar}\n{self.alaplap}\n{self.tapegyseg}\n{self.ram}"

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
            return f"Háttértár gyártója: {self.gyarto}, modell: {self.modell}, meret: {self.meret} GB, csatlakozás: {self.csatlakozas}"

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

        def __str__(self):
            return f"tapegyseg gyartoja: {self.gyarto}, modell: {self.modell}, teljesitmeny: {self.teljesitmeny}W"

    class RAM: 
        def __init__(self,  gyarto: str, modell: str, meret: int):
            super().__init__()
            self.gyarto: str = gyarto
            self.modell: str = modell
            self.meret: str = meret

        def __str__(self):
            return f"RAM gyartoja: {self.gyarto}, modell: {self.modell}, meret: {self.meret}GB"
    

            
    