class Alaplap: 
    def __init__(self, gyarto: str, modell: str, tipus: str, processzorFoglalat: str):
        super().__init__()
        self.gyarto: str = gyarto
        self.modell: str = modell
        self.tipus: str = tipus
        self.processzorFoglalat: str = processzorFoglalat

    def __str__(self):
        return f"Alaplap: {self.gyarto} {self.modell} {self.tipus} {self.processzorFoglalat}"
