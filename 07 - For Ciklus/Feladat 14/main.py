from os import system

start: int = None
end: int = None

print("kezdőérték: ",end="")
start = int(input())

print("végérték: ",end="")
end = int(input())

#5tel vagy 7tel osztható számok összege a nagyobb

sumOt = 0
sumHet = 0

for i in range(start, end, 1):
    if (i % 5 == 0):
        sumOt = sumOt + i
    elif (i % 7 == 0):
        sumHet = sumHet + i

print(sumOt, sumHet)

if sumOt > sumHet:
    print("5-tel osztható számok összege a nagyobb")
else:
    print("7-tel osztható számok összege a nagyobb")