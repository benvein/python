from os import system

month: str = input("írja a jelenlegi hónap nevét: ").lower().strip()

match month:
    case "január":
        print("1. hónap")
    case "február":
        print("2. hónap")
    case "március":
        print("3. hónap")
    case "április":
        print("4. hónap")
    case "május":
        print("5. hónap")
    case "június":
        print("6. hónap")
    case "július":
        print("7. hónap")
    case "augusztus":
        print("8. hónap")
    case "szeptember":
        print("9. hónap")
    case "október":
        print("10. hónap")
    case "november":
        print("11. hónap")
    case "december":
        print("12. hónap")
    case _:
        print("ilyen hónap nincs")