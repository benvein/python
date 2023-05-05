from mboard import *
from tap import *
from processzor import *
from gpu import *
from hdd import *
from ram import *
  
class Szamitogep:
    def __init__(self, processzor:Processzor, videokartya:Videokartya, hattertar:Hattertar, alaplap:Alaplap, tapegyseg:Tapegyseg, ram:RAM):
        super().__init__()
        self.processzor = processzor
        self.videokartya = videokartya
        self.hattertar = hattertar
        self.alaplap = alaplap
        self.tapegyseg = tapegyseg
        self.ram = ram

    def __str__(self):
        return f"{self.processzor}\n{self.videokartya}\n{self.hattertar}\n{self.alaplap}\n{self.tapegyseg}\n{self.ram}"

            
    