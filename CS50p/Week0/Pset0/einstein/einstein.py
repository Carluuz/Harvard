def main():
    m = int(input("input: "))
    m = einstein(m)
    print(f"E = {m}")


def einstein(m):
    c = 300000000
    e = m * (c**2)
    return e


main()

# E = mc^2
