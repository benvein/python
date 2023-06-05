class Nationality:
    def __init__(self) -> None:
        super().__init__()
        self.nations: int = 0
        self.countries: str = None
    
    def __str__(self) -> None:
        return f"{self.countries}: {self.nations}"