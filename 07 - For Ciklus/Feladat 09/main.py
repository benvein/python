from os import system

start: int = None
end: int = None

#csokkeno paros

print("kezdőérték: ",end="")
start = int(input())

print("végérték: ",end="")
end = int(input())

if end % 2 == 0:
    for i in range(end, start, -2):
        print(i)
else:
    for i in range(end-1, start, -2):
        print(i)