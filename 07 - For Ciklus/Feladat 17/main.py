from os import system

start: int = None
end: int = None

print("kezdőérték: ",end="")
start = int(input())

print("végérték: ",end="")
end = int(input())

sum = 0
osszeg = 0
atlag: float = None

for i in range(start, end, 1):
    sum += i
    osszeg += 1

atlag = sum/osszeg

print(f"sum: {sum}")
print(f"darabszám: {osszeg}")

print(atlag)