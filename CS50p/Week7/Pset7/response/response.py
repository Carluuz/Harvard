import validators


def main():
    valid = validators.email(input("Whats's your mail address? "))
    if valid:
        return print("Valid")
    else:
        return print("Invalid")


if __name__ == "__main__":
    main()
