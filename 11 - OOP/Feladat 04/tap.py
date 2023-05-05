class Tapegyseg:
    def __init__(self, gyarto: str, modell: str, teljesitmeny: int):
        super().__init__()
        self.gyarto: str = gyarto
        self.modell: str = modell
        self.teljesitmeny: int = teljesitmeny

    def __str__(self):
        return f"tapegyseg: {self.gyarto} {self.modell} {self.teljesitmeny}W"