def main():
    frac = input("Fraction: ").strip()
    perc = convert(frac)
    print(gauge(perc))

def convert(frac):
    try:
        x, y = map(int, frac.split("/", maxsplit=1))

        if y == 0:
            raise ZeroDivisionError
        if x > y:
            raise ValueError

        perc = round((x / y) * 100) if x != 0 else x
        return perc
    except ValueError, ZeroDivisionError:
        pass

def gauge(perc):
    if perc <= 1:
        return 'E'
    elif perc >= 99:
        return 'F'
    else:
        return f"{perc}%"

if __name__ == "__main__":
    main()
