var = input("input: ").lower().replace("-", " ").strip()

match var:
    case "42" | "forty two":
        print("Yes")
    case _:
        print("No")
