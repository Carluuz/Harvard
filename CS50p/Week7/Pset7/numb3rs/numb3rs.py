import re
import sys


def main():
    print(validate(input("IPv4 Address: ").strip()))


def validate(ip):
    try:
        ipv4 = re.fullmatch(r"(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})", ip)
        first, sec, third, forth = ipv4.groups()
        first, sec, third, forth = int(first), int(sec), int(third), int(forth)
        if -1 < first < 256:
            if -1 < sec < 256:
                if -1 < third < 256:
                    if -1 < forth < 256:
                        return True

        return False
    except AttributeError:
        return False


if __name__ == "__main__":
    main()
