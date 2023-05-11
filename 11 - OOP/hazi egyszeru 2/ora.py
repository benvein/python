class Ora:
    def __init__(self, marka: str, cikkszam: str, vizallosag: int, szerkezet: str):
        super().__init__()
        self.marka: str = marka
        self.cikkszam: str = cikkszam
        self.vizallosag: int = vizallosag
        self.szerkezet: str = szerkezet

    def __str__(self):
        return f"{self.marka} {self.cikkszam} vizallosag {self.vizallosag} BAR, szerkezet: {self.szerkezet}"