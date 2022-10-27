from os import system

brand: str = None
model: str = None
type: str = None
cubicCm: int = None
releaseDate: int = None

print("auto markaja: ",end="")
brand = str(input())

print("auto modellje: ",end="")
model = str(input())

print("auto megjelenési eve: ",end="")
releaseDate = int(input())

print("autó típusa: ",end="")
type = str(input())

print("motor térfogata: ",end="")
cubicCm = int(input())

system("cls")

print(f" Márka: {brand}\n Modell: {model}\n Megjelenési év: {releaseDate}\n Autó típusa: {type}\n Motor térfogata: {cubicCm}")