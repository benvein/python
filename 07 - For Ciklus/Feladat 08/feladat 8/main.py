from os import system

start: int = None
end: int = None

print("adja meg a kezdőértéket: ",end="")
start = int(input())

print("adja meg a végértéket: ",end="")
end = int(input())

#novekvo paratlan

if start % 2 == 0:
    for i in range(start+1, end, +2):
        print(i)
else:
    for i in range(start, end, +2):
        print(i)