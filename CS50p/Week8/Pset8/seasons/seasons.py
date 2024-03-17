from datetime import date, datetime
import sys
import inflect

p = inflect.engine()

def main():
    today = date.today()
    dob = input("Date of Birth: ")
    dob = get_dob(dob)
    dif = today - dob
    minutes = p.number_to_words((dif.days * 24 * 60), andword="").capitalize()
    print(f"{minutes} minutes")


def get_dob(dob):
    try:
        d = datetime.strptime(dob, "%Y-%m-%d")
        return date(d.year, d.month, d.day)
    except ValueError:
        ValueError
        sys.exit("That's not a valid date!")


if __name__ == "__main__":
    main()
