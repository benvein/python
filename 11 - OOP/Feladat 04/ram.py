class RAM: 
    def __init__(self,  gyarto: str, modell: str, meret: int):
        super().__init__()
        self.gyarto: str = gyarto
        self.modell: str = modell
        self.meret: str = meret

    def __str__(self):
        return f"RAM: {self.gyarto} {self.modell} {self.meret} GB"