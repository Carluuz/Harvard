store = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

def main():
    total = 0
    while True:
        try:
            price = get_price()
            total += price
            print(f"Total: ${total:.2f}")
        except EOFError:
            print()
            break

def get_price():
    while True:
        try:
            item = input("Item: ").strip().title()
            for food in store:
                if item in food:
                    return float(store[item])
        except TypeError:
            pass

main()

