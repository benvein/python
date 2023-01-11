from os import system

start: int = None
end: int = None
osszeg = 0

print("kezdőérték: ",end="")
start = int(input())

print("végérték: ",end="")
end = int(input())

for i in range(start, end+1, 2):
    osszeg += i
for i in range(start+1, end, 2):
    osszeg -= i
print(osszeg)

