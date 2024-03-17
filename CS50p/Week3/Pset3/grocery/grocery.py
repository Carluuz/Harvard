def main():
    items = get_items()
    items = sort_items(items)
    print_items(items)



def get_items():
    grocery = {}
    while True:
        try:
            item = input("").upper()
            if item in grocery:
                grocery[item] += 1
            else:
                grocery[item] = 1
        except EOFError:
            return grocery


def sort_items(items):
        return dict(sorted(items.items()))


def print_items(items):
    print()
    for key, value in items.items():
        print(f"{value} {key}")

main()
