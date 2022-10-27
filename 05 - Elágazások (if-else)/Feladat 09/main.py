from os import system

x: int = None
y: int = None

print("adja meg az x-et: ",end="")
x = int(input())

print("adja meg az y-t: ",end="")
y = int(input())

if (x % y == 0):
    print("y osztója x-nek")
else:
    print("y nem osztója x-nek")