from os import system

#intervallum (kezdő és végérték), csökkenő sorrend

a: int = None
b: int = None

print("adja meg az intervallum kezdőértékét: ",end="")
a = int(input())

print("adja meg az intervallum végértékét: ",end="")
b = int(input())

for i in range(b, a, -1):
    print(i)