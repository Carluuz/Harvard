import inflect

p = inflect.engine()

def main():
    names = get_names()
    print_names(names)


def get_names():
    names = []
    try:
        while True:
            name = input("Name: ").strip()
            names.append(name)
    except EOFError:
        print()
        return names



def print_names(names):
    print(f"Adieu, adieu, to {p.join(names)}")

main()
