from os import system

start: int = None
end: int = None

print("kezdőérték: ",end="")
start = int(input())

print("végérték: ",end="")
end = int(input())

sumParos = 0
sumParatlan = 0

for i in range(start, end):
    if i % 2 == 0:
        sumParos = sumParos + i
    else:
        sumParatlan += i

print(sumParos, sumParatlan)

if sumParos > sumParatlan:
    print("páros számok összege a nagyobb")
else:
    print("páratlan számok összege a nagyobb")