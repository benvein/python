from os import system

choice = ["1", "2", "3", "4"]

#1 = Coca Cola, 2 = Pepsi, 3 = Fanta, 4 = Sprite

print("adja meg melyik italt szeretné: ",end="")
choice = str(input())

match choice:
    case "1":
        print("Coca Cola")
    case "2":
        print("Pepsi")
    case "3":
        print("Fanta")
    case "4":
        print("Sprite")
