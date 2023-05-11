class Champion:
    def __init__(self, name: str, role: str, price: int, adaptiveType: str):
        super().__init__()
        self.name: str = name
        self.role: str = role
        self.price: int = price
        self.adaptiveType: str = adaptiveType

    def __str__(self):
        return f"név: {self.name}, ár: {self.price}BE, szerep: {self.role}, sebzés: {self.adaptiveType}"
