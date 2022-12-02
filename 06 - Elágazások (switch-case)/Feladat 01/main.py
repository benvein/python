from os import system

day = input("adja meg hanyadik nap van a héten: ")

match day:
    case "1":
        print("hétfő van")
    case "2":
        print("kedd van")
    case "3":
        print("szerda van")
    case "4":
        print("csütörtök van")
    case "5":
        print("péntek van")
    case "6":
        print("szombat van")
    case "7":
        print("vasárnap van")
    case _:
        print("7 nap van egy héten")