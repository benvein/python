class Car:
    def __init__(self) -> None:
        super().__init__()
        self.model: str = None
        self.mpg: float = 0
        self.cylinders: int = 0
        self.torque: float = 0
        self.horsepower: float = 0
        self.weight: int = 0
        self.acceleration: float = 0
        self.manufactureYear: int = 0
        self.origin: str = None

    def __str__(self) -> str:
        return f"{self.model}, {self.mpg} {self.cylinders} {self.torque} {self.horsepower} {self.weight} {self.acceleration} {self.manufactureYear} {self.origin}"