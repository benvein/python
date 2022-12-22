from os import system

rows = int(input("sorok száma: "))

for i in range(rows):
    for j in range(rows - i - 1):
        print(" ",end=" ")
    for k in range(2 * i + 1):
        print(k + 1,end=" ")
    print()