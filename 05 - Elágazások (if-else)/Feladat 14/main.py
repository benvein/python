from os import system

x: int = None
y: int = None
z: int = None

print("x: ",end="")
x = int(input())

print("y: ",end="")
y = int(input())

print("z: ",end="")
z = int(input())

if (x % y == 0 or x % z == 0 or (x % y == 0 and x % z == 0)):
    if (x % y == 0 and x % z != 0):
        print("x oszható y-nal")
    elif (x % z == 0 and x % y != 0):
        print("x oszható z-vel")
    else:
        print("x oszható y-nal és z-vel is")
else:
    print("x sem z-vel sem y-nal nem osztható")