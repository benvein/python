class Motorcycle:
    def __init__(self):
        super().__init__()
        self.manufacturer: str = None
        self.type: str = None
        self.model: str = None
        self.fuelConsumption: float = 0
        self.productionYear: int = 0
        self.torque: int = 0
        self.cylinders: int = 0
        self.horsepower: int = 0

    #magic methods
    def __str__(self) -> str:
        return f"{self.manufacturer} {self.model} ({self.productionYear})"