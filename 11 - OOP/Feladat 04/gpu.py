class Videokartya:
    def __init__(self, gyarto: str, modell: str, vram: int):
        super().__init__()
        self.gyarto: str = gyarto
        self.modell: str = modell
        self.vram: int = vram
    
    def __str__(self):
        return f"videókártya: {self.gyarto} {self.modell} {self.vram} GB"
