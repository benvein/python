from os import system

start: int = None
end: int = None

print("kezdőérték: ",end="")
start = int(input())

print("végérték: ",end="")
end = int(input())

osszeg = 0

for i in range(start, end, 1):
    if i % 2 != 0:
        if i % 3 == 0:
            osszeg += 1
print(osszeg)