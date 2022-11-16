from os import system

#előétel
zoldsegleves: bool = False
husleves: bool = False
gyumolcsleves: bool = False
#főétel
sultCsirkecomb: bool = False
sultCsirkemell: bool = False
rakottzoldseg: bool = False
spagetti: bool = False
pizza: bool = False
#köret
rizs: bool = False
paroltzoldseg: bool = False
gyumolcs: bool = False
sultkrumpli: bool = False
salata: bool = False
kola: bool = False
#valasztott
eloetel: int = None
foetel: int = None
koret: int = None

print("Előétel: zöldségleves(1), húsleves(2), gyumolcsleves(3): ",end="")
eloetel = int(input())
if (eloetel == 1):
    zoldsegleves: bool = True
elif (eloetel == 2):
    husleves: bool = True
elif (eloetel == 3):
    gyumolcsleves: bool = True

print("Főétel: Sult csirkecomb(1), sult csirkemell(2), rakottzöldség(3), spagetti(4), pizza(5): ",end="")
foetel = int(input())
if (foetel == 1):

print("Köret: rizs(1), pároltzöldség(2), gyümölcs(3), sültkrumpli(4), saláta(5), kóla(6): ",end="")
koret = int(input())