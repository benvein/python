from os import system
system("cls")

x: int = 9
y: int = 3

def muveletek(x: int, y: int) -> int:
    osszeadas = x + y
    kivonas = x - y
    szorzas = x * y
    osztas: float = x / y
    return osszeadas, kivonas, szorzas, osztas

osszeadas: int = osszeadas(x, y)
kivonas: int = kivonas(x, y)

print(f"osszeadas eredmenye: {osszeadas}")