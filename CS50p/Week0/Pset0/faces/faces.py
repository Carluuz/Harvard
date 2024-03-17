def main():
    variable = input("input: ")
    variable = convert(variable)
    print(variable)


def convert(text):
    text = text.replace(":)", "🙂")
    text = text.replace(":(", "🙁")
    return text


main()
