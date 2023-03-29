from os import system
from consoleio import *
from funcitons import *

system("cls")

nev1: str = nevBekeres()
oraszam1: int = oraBekeres()
ber1: int = berKiszamitas(oraszam1)

nev2: str = nevBekeres()
oraszam2: int = oraBekeres()
ber2: int = berKiszamitas(oraszam2)

nev3: str = nevBekeres()
oraszam3: int = oraBekeres()
ber3: int = berKiszamitas(oraszam3)

nev4: str = nevBekeres()
oraszam4: int = oraBekeres()
ber4: int = berKiszamitas(oraszam4)

nev5: str = nevBekeres()
oraszam5: int = oraBekeres()
ber5: int = berKiszamitas(oraszam5)

kiiratas(nev1, oraszam1, ber1, nev2, oraszam2, ber2, nev3, oraszam3, ber3, nev4, oraszam4, ber4, nev5, oraszam5, ber5)