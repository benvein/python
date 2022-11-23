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
    sultCsirkecomb: bool = True
elif (foetel == 2):
    sultCsirkemell: bool = True
elif (foetel == 3):
    rakottzoldseg: bool = True
elif (foetel == 4):
    spagetti: bool = True
elif (foetel == 5):
    pizza: bool = True

print("Köret: rizs(1), pároltzöldség(2), gyümölcs(3), sültkrumpli(4), saláta(5), kóla(6): ",end="")
koret = int(input())
if (koret == 1):
    rizs: bool = True
elif (koret == 2):
    paroltzoldseg: bool = True
elif (koret == 3):
    gyumolcs: bool = True
elif (koret == 4):
    sultkrumpli: bool = True
elif (koret == 5):
    salata: bool = True
elif (koret == 6):
    kola: bool = True

if (zoldsegleves and spagetti and (gyumolcs or salata) and (pizza != True and rakottzoldseg != True)):
    print("kiváló értékelésű a menü")
elif (zoldsegleves and sultCsirkemell and rizs and sultkrumpli != True):
    print("fitnesz menü")
elif (husleves and sultCsirkecomb and (sultkrumpli or salata) and (pizza != True and rakottzoldseg != True)):
    print("vasárnapi menü")
elif ((pizza or spagetti) and (gyumolcs or kola) and (rakottzoldseg != True and paroltzoldseg != True)):
    print("napi menü")