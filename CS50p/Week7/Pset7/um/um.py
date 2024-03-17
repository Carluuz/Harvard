import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    count = 0
    finds = re.findall(r'(?<![^\W])um(?![^\W])', s, flags=re.IGNORECASE)
    count = len(finds)
    print(finds)
    return count


if __name__ == "__main__":
    main()
