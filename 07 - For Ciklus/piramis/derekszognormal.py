from os import system

rows = int(input("number of rows: "))

for i in range(rows):
    for j in range(i+1):
        print(f"{j+1}",end="  ")
    print("\n")