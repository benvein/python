class Pingvin:
    def __init__(self, nev: str, eletkor: int, tomeg: int):
        super().__init__()
        self.nev: str = nev
        self.eletkor: int = eletkor
        self.tomeg: int = tomeg

    def __str__(self):
        return f"Pingvin neve {self.nev}, {self.eletkor} éves és {self.tomeg} kg"