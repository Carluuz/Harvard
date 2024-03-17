import re


def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if p_length(s) == False:
        return False
    if first_two(s) == False:
        return False
    if mid_numbs(s) == False:
        return False
    if first_num(s) == False:
        return False
    if other_chars(s) == False:
        return False

    return True


def p_length(s):
    if 2 <= len(s) <= 6:
        return True

    return False


def first_two(s):
    if s[:2].isalpha():
        return True

    return False


def mid_numbs(s):
    first_n = None
    for i, c in enumerate(s):
        if c.isdigit():
            first_n = i
            break

    if first_n is not None:
        temp = s[first_n:]
        return temp.isdigit()

    return True


def first_num(s):
    temp = re.sub("[a-zA-Z]", "", s)
    for l in temp:
        if l.isdigit():
            if l == "0":
                return False
            break

    return True


def other_chars(s):
    return s.isalnum()


if __name__ == "__main__":
    main()
