class Processzor:
    def __init__(self, gyarto: str, modell: str, magok: int):
        super().__init__()
        self.gyarto: str = gyarto
        self.modell: str = modell
        self.magok: int = magok

    def __str__(self):
        return f"processzor: {self.gyarto} {self.modell} {self.magok} mag"
