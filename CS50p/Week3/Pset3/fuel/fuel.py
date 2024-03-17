def main():
    perc = int(get_input())
    if perc <= 1:
        print("E")
    elif perc >= 99:
        print("F")
    else:
        print(f"{perc}%")


def get_input():
    frac = input("Fraction: ").strip()

    if '/' in frac:
        x, y = frac.split("/", maxsplit=1)
    else:
        return get_input()

    if x.isdigit() and y.isdigit():
        x = float(x)
        y = float(y)
        if x <= y and y != 0:
            if x == 0:
                return x
            return round((x / y) * 100)
        else:
            return get_input()
    else:
        return get_input()

main()
