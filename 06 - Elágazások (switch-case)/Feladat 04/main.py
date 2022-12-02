from os import system

num1: int = None
num2: int = None
operation: str = None
result: float = None

print("adjon meg egy egész számot: ",end="")
num1 = int(input())

print("adjon meg még egyet: ",end="")
num2 = int(input())

print("adjon meg egy műveletet [+,-,*,/]: ",end="")
operation = str(input())

match operation:
    case "+":
        result = num1 + num2
        print(f"a végeredmény {result}")
    case "-":
        result = num1 - num2
        print(f"a végeredmény {result}")
    case "*":
        result = num1 * num2
        print(f"a végeredmény {result}")
    case "/":
        result = num1 / num2
        print(f"a végeredmény {result}")
    case _:
        print("ilyen művelet nincs")