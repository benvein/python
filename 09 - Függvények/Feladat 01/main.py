from os import system
system("cls")

def osszeadas(a: int, b: int) -> int:
    vegeredmeny: int = a + b
    return vegeredmeny

def kivonas(a: int, b: int) -> int:
    vegeredmeny: int = a - b
    return vegeredmeny

def szorzas(a: int, b: int) -> int:
    vegeredmeny: int = a * b
    return vegeredmeny

def osztas(a: int, b: int) -> float:
    vegeredmeny: float = a / b
    return vegeredmeny

a: int = 9
b: int = 3

eredmenyOsszeadas: int = osszeadas(a, b)
eredmenyKivonas: int = kivonas(a, b)
eredmenySzorzas: int = szorzas(a, b)
eredmenyOsztas:  float = osztas(a, b)

print(f"{eredmenyOsszeadas}, {eredmenyKivonas}, {eredmenySzorzas}, {eredmenyOsztas}")