from allatok import *
from os import system

system("cls")

medve: Medve = Medve("Dagadt", 30, 400)
pingvin: Pingvin = Pingvin("Nagypofájú", 10, 30)
oroszlan: Oroszlan = Oroszlan("Pébesz", 14, 243)
elefant: Elefant = Elefant("Dagadtabb", 64, 1673)
zebra: Zebra = Zebra("Nagyoncsíkos", 12, 143)
tigris: Tigris = Tigris("Kicsitcsíkos", 26, 123)

allatok: Allatok = Allatok(medve, pingvin, oroszlan, elefant, zebra, tigris)

print(f"{allatok}")