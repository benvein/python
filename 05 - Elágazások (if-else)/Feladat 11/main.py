from os import system

num: int = None

print("adjon meg egy szamot: ",end="")
num = int(input())

if (num % 2 == 0 and num % 5 == 0 and 0 < num):
    print("a szám páros, oszható 5-tel és pozitív")

elif (num % 2 == 0 and num % 5 != 0 and 0 < num):
    print("a szám páros, nem osztható 5-tel és pozitív")

elif (num % 2 == 0 and num % 5 == 0 and num < 0):
    print("a szám páros, osztható 5-tel és negatív")

elif (num % 2 == 0 and num % 5 != 0 and num < 0):
    print("a szám páros, nem oszható 5-tel és negatív")

elif (num % 2 != 0 and num % 5 == 0 and 0 < num):
    print("a szám páratlan, oszható 5-tel és pozitív")

elif (num % 2 != 0 and num % 5 != 0 and 0 < num):
    print("a szám páratlan, nem oszható 5-tel és pozitív")

elif (num % 2 != 0 and num % 5 == 0 and num < 0):
    print("a szám páratlan, oszható 5-tel és negatív")

elif (num % 2 != 0 and num % 5 != 0 and num < 0):
    print("a szám páratlan, nem osztható 5-tel és negatív")
    
else:
    print("0 a szám")