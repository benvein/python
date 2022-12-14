from os import system

start: int = None
end: int = None

print("kezdőérték: ",end="")
start=int(input())

print("végérték: ",end="")
end = int(input())

#páros sum, páratlan szorzat

sum = 0
szorzat: int = 1

for i in range(start, end, 1):
    if i % 2 == 0:
        sum = sum + i
    else:
        szorzat = szorzat * i

print(sum, szorzat)
    