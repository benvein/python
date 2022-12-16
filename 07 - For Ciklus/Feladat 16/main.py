from os import system

start: int = None
end: int = None

print("kezdőérték: ",end="")
start = int(input())

print("végérték: ",end="")
end = int(input())

#paros paratlan szamok osszege atlaga

sumParos = 0
sumParatlan = 0
osszegParos = 0
osszegParatlan = 0
atlag: float = None

for i in range(start, end, 1):
    if i % 2 == 0:
        sumParos += i
        osszegParos += 1
    else:
        sumParatlan += i
        osszegParatlan += 1

atlag = (sumParos + sumParatlan) / (osszegParos + osszegParatlan)

print(atlag)