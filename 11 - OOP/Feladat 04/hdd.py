class Hattertar:
    def __init__(self, gyarto: str, modell: str, meret: int, csatlakozas: str):
        super().__init__()
        self.gyarto: str = gyarto
        self.modell: str = modell
        self.meret: int = meret
        self.csatlakozas: str = csatlakozas

    def __str__(self):
        return f"Háttértár: {self.gyarto} {self.modell} {self.meret} GB {self.csatlakozas}"