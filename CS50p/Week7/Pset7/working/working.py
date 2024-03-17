import re
import sys


def main():
    print(convert(input("Hours: ").strip()))


def convert(s):
    time = re.fullmatch(r"(\d{1,2}:?(?:\d{1,2})?) ([ap]m) to (\d{1,2}:?(?:\d{1,2})?) ([ap]m)", s, re.IGNORECASE)
    # convert input to variables
    if not time == None:
        start_t, start_p, end_t, end_p = time.groups()

        if ":" in start_t:
            start_h, start_m = start_t.split(":")
        else:
            start_h = start_t
            start_m = 0

        if ":" in end_t:
            end_h, end_m = end_t.split(":")
        else:
            end_h = end_t
            end_m = 0

        start_h, start_m, end_h, end_m = int(start_h), int(start_m), int(end_h), int(end_m)
        start_p, end_p = start_p.lower(), end_p.lower()

    else:
        raise ValueError

    # check time
    if not 0 <= start_h <= 12 or not 0 <= end_h <= 12:
        raise ValueError
    if start_h == 12:
        start_h = 0
    if end_h == 12:
        end_h = 0

    if not 0 <= start_m < 60 or not 0 <= end_m < 60:
        raise ValueError

    # check period, and change time if needed
    if start_p == 'pm':
        start_h += 12

    if end_p == 'pm':
        end_h += 12

    return f'{start_h:02d}:{start_m:02d} to {end_h:02d}:{end_m:02d}'

if __name__ == "__main__":
    main()
