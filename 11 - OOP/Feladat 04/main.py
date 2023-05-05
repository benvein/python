from szamitogep import *

processzor: Processzor = Processzor("Intel", "Pentium", 4)
videokartya: Videokartya = Videokartya("Nvidia", "GT910", 1)
hattertar: Hattertar = Hattertar("Kingston", "W1000", 1000, "SATA6")
alaplap: Alaplap = Alaplap("Asus", "ROG strix", "ATX", "Intel 9th gen")
tapegyseg: Tapegyseg = Tapegyseg("NZXT", "idk", 1000)
ram: RAM = RAM("Kingston", "eztsetudom", 8)

pc: Szamitogep = Szamitogep(processzor, videokartya, hattertar, alaplap, tapegyseg, ram)

print(f"{pc}")