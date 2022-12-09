from os import system

start: int = None
end: int = None

print("kezdőérték: ",end="")
start = int(input())

print("végérték: ",end="")
end = int(input())

sum = 0
for i in range(start, end):
    sum = sum + i

print(sum)