from os import system
import random
system("cls")

#Egy zsákba 20 labda van. Az egyik csapat a zsákba rakja a labdát (gyűjtök). A másik csapat a zsákból veszi ki a labdát (fogyasztók).
#A gyűjtők 0-5 közötti véletlen számú labdával dolgoznak. A fogyasztók 0-10 közötti véletlen számú labdával dolgoznak. Egy menetben gyűjtés és fogyasztás is történik.
#Szimulálja a játékot. Minden lépésbe írja ki a gyűjtők ás a fogyasztók hány labdával dolgoztak, valamit, hogy hány labda van a zsákban.
#A játék szimuláció addig tart, amíg a zsák ki nem ürül (a végén a zsákba negatív számú labda is lehet, evvel most ne foglalkozzon).

#A játék során határozza meg:
# - mennyi volt  egy adott lépésben a legtöbb labda a zsákba
# - hányszor volt a gyűjtőknél több labda mint a fogyasztóknál
# - hányszor volt a gyűjtőknél kevesebb labda mint a fogyasztóknál
# - hányszor volt a gyűjtőknél ugyan annyi labda mint a fogyasztóknál

zsak: int = 20
gyujtok: int = random.randint(0, 5)
fogyasztok: int = random.randint(0, 10)

while (zsak<20):
    zsak - (gyujtok + fogyasztok)