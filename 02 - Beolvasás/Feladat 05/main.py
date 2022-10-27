from os import system

band: str = None
song: str = None
lenght: int = None

print("kedvenc banda: ")
band = str(input())

print("kedvenc dal: ")
song = str(input())

print("dal hossza percben: ")
lenght = int(input())

system("cls")

print(f"Az ön kedvenc együttesének neve {band} a legjobb zeneszáma {song} melynek hossza {lenght} perc")