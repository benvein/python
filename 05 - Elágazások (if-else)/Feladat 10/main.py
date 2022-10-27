from os import system

num: int = None

print("adjon meg egy egesz szamot: ",end="")
num = int(input())

if (num % 2 == 0 and num % 3 != 0):
    print("BIZ")
elif (num % 3 == 0 and num % 2 != 0):
    print("BAZ")
elif (num % 2 == 0 and num % 3 == 0):
    print("ZIZI")