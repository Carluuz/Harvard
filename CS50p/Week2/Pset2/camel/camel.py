def main():
    camel = get_input()
    normal = separate(camel)
    snake = convert(normal)
    print(f"snake_case: {snake}")


def get_input():
    x = input("camelCase: ").replace(" ", "")
    return x


def separate(y):
    temp = ""
    for i in y:
        if i.islower():
            temp = temp + i
        else:
            temp = temp + " " + i.lower()

    return temp


def convert(z):
    z = z.replace(" ", "_")
    return z

main()
