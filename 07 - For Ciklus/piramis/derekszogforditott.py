from os import system

rows = int(input("sorok száma: "))

for i in range(rows, 0, -1):
    for j in range(1, i+1):
        print(j, end="   ")

    print("\n")
